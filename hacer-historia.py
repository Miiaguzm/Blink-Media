#!/usr/bin/env python3
"""
Monta la plantilla de historia de Blink encima de un video, sin navegador.

El generador hace lo mismo en el navegador de Mia, pero ahí depende de
MediaRecorder, que en Safari congela la imagen y corta el audio. Esto corre con
ffmpeg, así que no se pega ni se corta: el resultado es el mismo archivo cada vez.

Uso:
    python3 hacer-historia.py entrada.mov salida.mp4 \
        --rotulo "EN VIVO" \
        --titular "Katteyes se subió a una Ducati en el Movistar Arena" \
        [--cuenta @blinkmediacl] [--zoom 1.0] [--posx 50] [--pos 50]

El encuadre funciona igual que en el generador: zoom 1 llena la historia, y
posx/pos reparten el sobrante cuando el video no viene en 9:16.
"""

import argparse, json, os, shutil, subprocess, sys, tempfile, urllib.parse

AQUI = os.path.dirname(os.path.abspath(__file__))
PLANTILLA = os.path.join(AQUI, "historia-video.html")
CHROMIUM = "/opt/pw-browsers/chromium"
ANCHO, ALTO = 1080, 1920

# El titineo aprobado: destello corto, corto, uno más largo, y recién ahí fijo.
# La salida es el mismo patrón en espejo. Son segundos desde que arranca el tramo.
ENTRA = [(0, 0.067), (0.133, 0.200), (0.233, 0.333)]
FIJO = 0.400
SALE = [(0.100, 0.167), (0.233, 0.300), (0.367, 0.433)]
FIN = 0.467


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
    # Un video grabado en vertical con el teléfono suele venir tumbado con una
    # rotación en los metadatos: lo que importa es cómo se ve, no cómo se guardó.
    rot = 0
    for lado in (v.get("side_data_list") or []):
        if "rotation" in lado:
            rot = abs(int(lado["rotation"])) % 180
    w, h = int(v["width"]), int(v["height"])
    if rot == 90:
        w, h = h, w
    return w, h, float(d["format"]["duration"]), hay_audio


def tiempos(dur):
    entra = max(0.12, dur * 0.10) if dur < 3.2 else 0.80
    sale = dur - FIN - 0.05
    if sale <= entra + FIJO + 0.5:
        sale = None          # muy corto para apagarse: se queda hasta el final
    return entra, sale


def compuerta(dur):
    """La expresión enable: el logo y el texto prenden y apagan en el mismo cuadro."""
    entra, sale = tiempos(dur)
    tramos = [(entra + a, entra + b) for a, b in ENTRA]
    if sale is None:
        tramos.append((entra + FIJO, dur + 1))
    else:
        tramos.append((entra + FIJO, sale))
        tramos += [(sale + a, sale + b) for a, b in SALE]
    return "+".join("between(t,%.3f,%.3f)" % t for t in tramos)


def capas(carpeta, rotulo, titular, cuenta):
    base = "file://" + urllib.parse.quote(PLANTILLA)
    q = urllib.parse.urlencode({"rotulo": rotulo, "titular": titular, "cuenta": cuenta})
    salidas = {}
    for capa in ("logo", "velo", "texto"):
        crudo = os.path.join(carpeta, "crudo-%s.png" % capa)
        correr([CHROMIUM, "-headless=new", "--no-sandbox", "--disable-gpu",
                "--hide-scrollbars", "--force-device-scale-factor=1",
                "--window-size=%d,%d" % (ANCHO, ALTO + 90),
                "--allow-file-access-from-files",
                "--default-background-color=00000000",
                "--virtual-time-budget=9000",
                "--screenshot=" + crudo,
                "%s?%s&capa=%s" % (base, q, capa)])
        # Chromium pinta de menos, así que se rinde más alto y se recorta.
        corte = os.path.join(carpeta, "%s.png" % capa)
        correr(["ffmpeg", "-v", "error", "-i", crudo,
                "-vf", "crop=%d:%d:0:0" % (ANCHO, ALTO), corte, "-y"])
        salidas[capa] = corte
    return salidas


def main():
    p = argparse.ArgumentParser()
    p.add_argument("entrada"); p.add_argument("salida")
    p.add_argument("--rotulo", default="EN VIVO")
    p.add_argument("--titular", required=True)
    p.add_argument("--cuenta", default="@blinkmediacl")
    p.add_argument("--zoom", type=float, default=1.0)
    p.add_argument("--posx", type=float, default=50)
    p.add_argument("--pos", type=float, default=50)
    p.add_argument("--sin-audio", action="store_true")
    # Para cortar un video largo. El punto no se elige por reloj: se buscan los
    # cambios de escena con select='gt(scene,0.25)' y se cruza con el nivel del
    # audio por ventanas de 1 s, para no cortar a alguien a mitad de una frase.
    p.add_argument("--hasta", type=float, default=None,
                   help="corta el video a estos segundos")
    # 23 deja el archivo cerca del peso del original. Bajarlo engorda el archivo
    # sin que se note, porque la calidad no puede subir más que la del video que ella mandó.
    p.add_argument("--crf", default="23")
    a = p.parse_args()

    for f in (PLANTILLA, os.path.join(AQUI, "logo-blink.png")):
        if not os.path.exists(f):
            sys.exit("falta " + f)

    w, h, dur, hay_audio = sondear(a.entrada)
    # El recorte se aplica antes de calcular los tiempos, para que la animación
    # de salida caiga dentro del trozo que queda y no del video entero.
    if a.hasta and a.hasta < dur:
        dur = a.hasta
    esc = max(ANCHO / w, ALTO / h) * a.zoom
    aw, ah = w * esc, h * esc
    x, y = (aw - ANCHO) * a.posx / 100, (ah - ALTO) * a.pos / 100
    print("entrada: %dx%d, %.1f s, audio: %s" % (w, h, dur, "sí" if hay_audio else "no"))

    carpeta = tempfile.mkdtemp(prefix="blink-historia-")
    try:
        c = capas(carpeta, a.rotulo, a.titular, a.cuenta)
        entra, sale = tiempos(dur)
        gate = compuerta(dur)
        velo_sale = (sale + FIN) if sale is not None else (dur + 1)

        filtro = (
            "[0:v]scale={aw}:{ah}:flags=lanczos,crop={W}:{H}:{x}:{y},"
            "fps=30,format=rgba[base];"
            "[1:v]format=rgba,fade=t=in:st={vi}:d=0.45:alpha=1,"
            "fade=t=out:st={vo}:d=0.40:alpha=1[velo];"
            "[2:v]format=rgba[logo];[3:v]format=rgba[txt];"
            "[base][velo]overlay=0:0[v1];"
            "[v1][logo]overlay=0:0:enable='{g}'[v2];"
            "[v2][txt]overlay=0:0:enable='{g}'[out]"
        ).format(aw=round(aw), ah=round(ah), W=ANCHO, H=ALTO,
                 x=round(x), y=round(y),
                 vi=max(0, entra - 0.10), vo=velo_sale, g=gate)

        cmd = ["ffmpeg", "-v", "error"]
        if a.hasta:
            cmd += ["-t", "%.3f" % dur]
        cmd += ["-i", a.entrada]
        for capa in ("velo", "logo", "texto"):
            cmd += ["-loop", "1", "-t", "%.3f" % (dur + 1), "-i", c[capa]]
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
