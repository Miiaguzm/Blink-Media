#!/usr/bin/env python3
"""
Monta una lámina de carrusel de Blink (1080×1350) con un video adentro.

Es el hermano de hacer-historia.py: mismo motivo —el generador depende de
MediaRecorder, que en Safari congela la imagen y corta el audio— y misma salida,
ffmpeg en vez de navegador, así que da el mismo archivo siempre.

El encuadre replica dibujarLamina() del generador: márgenes de 72, tope en 195,
el video centrado en el espacio libre y el texto 34px debajo, en Montserrat 600
de 33px. El video va enmarcado y no a sangre, que es lo que corresponde cuando
el material ya trae su propio texto encima.

Uso:
    python3 hacer-lamina.py entrada.mp4 salida.mp4 \
        --texto "Entradas disponibles a través de portaldisc.com" \
        [--tam 100] [--desenfoque 26] [--brillo 0.9] [--crf 23]
"""

import argparse, json, math, os, shutil, subprocess, sys, tempfile, urllib.parse

AQUI = os.path.dirname(os.path.abspath(__file__))
PLANTILLA = os.path.join(AQUI, "lamina-video.html")
CHROMIUM = "/opt/pw-browsers/chromium"
ANCHO, ALTO = 1080, 1350

# Las constantes de dibujarLamina() en generador.html.
MARGEN = 72
ANCHO_L = ANCHO - MARGEN * 2      # 936
TOPE = 195
PIE = 70
INTERLINEA = 47.9
GAP = 34
MAX_TEXTO = 880                   # ancho máximo de una línea de texto


def correr(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.exit("falló: " + " ".join(cmd[:3]) + "…\n" + (r.stderr or "")[-1500:])
    return r.stdout


def sondear(video):
    s = correr(["ffprobe", "-v", "error", "-print_format", "json",
                "-show_streams", "-show_format", video])
    d = json.loads(s)
    v = next((x for x in d["streams"] if x["codec_type"] == "video"), None)
    if not v:
        sys.exit("ese archivo no trae pista de video")
    hay_audio = any(x["codec_type"] == "audio" for x in d["streams"])
    rot = 0
    for lado in (v.get("side_data_list") or []):
        if "rotation" in lado:
            rot = abs(int(lado["rotation"])) % 180
    w, h = int(v["width"]), int(v["height"])
    if rot == 90:
        w, h = h, w
    return w, h, float(d["format"]["duration"]), hay_audio


def lineas_de(texto):
    """Cuántas líneas ocupa el texto, midiéndolas en el navegador y no a ojo.

    El reparto tiene que dar el mismo número que el del generador, porque de él
    depende dónde queda el video: una línea de más lo sube 48px.
    """
    if not texto.strip():
        return 0
    pagina = """<meta charset="utf-8"><body style="margin:0">
<span id="m" style="font:600 33px Montserrat,sans-serif;white-space:nowrap;
letter-spacing:.1px;position:absolute;visibility:hidden"></span>
<div id="r">?</div>
<script>
  const el = document.getElementById("m");
  const palabras = %s.split(/\\s+/);
  let n = 1, act = "";
  for (const p of palabras){
    el.textContent = act ? act + " " + p : p;
    if (el.getBoundingClientRect().width > %d && act){ n++; act = p; }
    else { act = el.textContent; }
  }
  document.getElementById("r").textContent = "LINEAS=" + n;
</script>""" % (json.dumps(texto), MAX_TEXTO)
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "medir.html")
        open(f, "w").write(pagina)
        dom = correr([CHROMIUM, "-headless=new", "--no-sandbox", "--disable-gpu",
                      "--virtual-time-budget=5000", "--dump-dom",
                      "file://" + urllib.parse.quote(f)])
    marca = "LINEAS="
    if marca not in dom:
        sys.exit("no se pudo medir el texto en el navegador")
    return int(dom.split(marca)[1].split("<")[0].strip())


def capas(carpeta, texto, rect):
    base = "file://" + urllib.parse.quote(PLANTILLA)
    q = urllib.parse.urlencode({"texto": texto, "rx": rect[0], "ry": rect[1],
                                "rw": rect[2], "rh": rect[3]})
    salidas = {}
    for capa in ("velo", "marca"):
        crudo = os.path.join(carpeta, "crudo-%s.png" % capa)
        correr([CHROMIUM, "-headless=new", "--no-sandbox", "--disable-gpu",
                "--hide-scrollbars", "--force-device-scale-factor=1",
                "--window-size=%d,%d" % (ANCHO, ALTO + 90),
                "--allow-file-access-from-files",
                "--default-background-color=00000000",
                "--virtual-time-budget=9000",
                "--screenshot=" + crudo,
                "%s?%s&capa=%s" % (base, q, capa)])
        corte = os.path.join(carpeta, "%s.png" % capa)
        correr(["ffmpeg", "-v", "error", "-i", crudo,
                "-vf", "crop=%d:%d:0:0" % (ANCHO, ALTO), corte, "-y"])
        salidas[capa] = corte
    return salidas


def mascara(carpeta, w, h, radio=24):
    """Un PNG blanco con las esquinas redondeadas, para recortar el video."""
    f = os.path.join(carpeta, "mascara.html")
    open(f, "w").write(
        "<meta charset=utf-8><style>html,body{margin:0;background:#000}"
        "div{width:%dpx;height:%dpx;background:#fff;border-radius:%dpx}</style><div></div>"
        % (w, h, radio))
    crudo = os.path.join(carpeta, "crudo-mascara.png")
    correr([CHROMIUM, "-headless=new", "--no-sandbox", "--disable-gpu",
            "--hide-scrollbars", "--force-device-scale-factor=1",
            "--window-size=%d,%d" % (w, h + 90),
            "--virtual-time-budget=4000",
            "--screenshot=" + crudo, "file://" + f])
    corte = os.path.join(carpeta, "mascara.png")
    correr(["ffmpeg", "-v", "error", "-i", crudo,
            "-vf", "crop=%d:%d:0:0,format=gray" % (w, h), corte, "-y"])
    return corte


def main():
    p = argparse.ArgumentParser()
    p.add_argument("entrada"); p.add_argument("salida")
    p.add_argument("--texto", default="")
    p.add_argument("--tam", type=float, default=100)
    p.add_argument("--desenfoque", type=float, default=26)
    p.add_argument("--brillo", type=float, default=0.9)
    p.add_argument("--crf", default="23")
    p.add_argument("--sin-audio", action="store_true")
    a = p.parse_args()

    for f in (PLANTILLA, os.path.join(AQUI, "logo-blink.png")):
        if not os.path.exists(f):
            sys.exit("falta " + f)

    w, h, dur, hay_audio = sondear(a.entrada)

    # ---- dónde va el video, con las cuentas del generador ----
    n = lineas_de(a.texto)
    alto_texto = n * INTERLINEA
    gap = GAP if n else 0
    disponible = ALTO - TOPE - PIE
    alto_libre = disponible - gap - alto_texto
    calce = min(ANCHO_L / w, alto_libre / h)
    rw = w * calce * (a.tam / 100)
    rh = h * calce * (a.tam / 100)
    total = rh + gap + alto_texto
    ry = TOPE + max(0, (disponible - total) / 2)
    rx = ANCHO / 2 - rw / 2
    # Pares, porque libx264 con yuv420p no acepta impares en el overlay.
    rw, rh = int(rw // 2 * 2), int(rh // 2 * 2)
    rx, ry = int(round(rx)), int(round(ry))

    print("entrada: %dx%d, %.1f s, audio: %s" % (w, h, dur, "sí" if hay_audio else "no"))
    print("marco:   %dx%d en (%d, %d) · %d línea(s) de texto" % (rw, rh, rx, ry, n))

    carpeta = tempfile.mkdtemp(prefix="blink-lamina-")
    try:
        c = capas(carpeta, a.texto, (rx, ry, rw, rh))
        msk = mascara(carpeta, rw, rh)

        # El fondo es el mismo video, a sangre, desenfocado y más oscuro. Se
        # escala a cubrir 1080×1350 y se recorta al centro.
        esc = max(ANCHO / w, ALTO / h)
        fw, fh = int(round(w * esc)), int(round(h * esc))
        fx, fy = (fw - ANCHO) // 2, (fh - ALTO) // 2

        filtro = (
            "[0:v]split=2[bg][fg];"
            "[bg]scale={fw}:{fh}:flags=lanczos,crop={W}:{H}:{fx}:{fy},"
            "gblur=sigma={sig},eq=brightness={br},fps=30,format=rgba[fondo];"
            "[fg]scale={rw}:{rh}:flags=lanczos,fps=30,format=rgba[marco];"
            "[3:v]format=gray[msk];"
            "[marco][msk]alphamerge[marcoR];"
            "[fondo][1:v]overlay=0:0[v1];"
            "[v1][marcoR]overlay={rx}:{ry}[v2];"
            "[v2][2:v]overlay=0:0[out]"
        ).format(fw=fw, fh=fh, W=ANCHO, H=ALTO, fx=fx, fy=fy,
                 sig=a.desenfoque, br=round(a.brillo - 1, 3),
                 rw=rw, rh=rh, rx=rx, ry=ry)

        cmd = ["ffmpeg", "-v", "error", "-i", a.entrada]
        for f in (c["velo"], c["marca"], msk):
            cmd += ["-loop", "1", "-t", "%.3f" % (dur + 1), "-i", f]
        cmd += ["-filter_complex", filtro, "-map", "[out]"]
        if hay_audio and not a.sin_audio:
            cmd += ["-map", "0:a", "-c:a", "aac", "-b:a", "192k", "-ar", "48000"]
        else:
            cmd += ["-an"]
        cmd += ["-c:v", "libx264", "-preset", "slow", "-crf", a.crf,
                "-profile:v", "high", "-pix_fmt", "yuv420p",
                "-movflags", "+faststart", "-shortest", a.salida, "-y"]
        correr(cmd)
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)

    w2, h2, dur2, audio2 = sondear(a.salida)
    print("salida:  %dx%d, %.1f s, audio: %s" % (w2, h2, dur2, "sí" if audio2 else "no"))
    print("listo:", a.salida)


if __name__ == "__main__":
    main()
