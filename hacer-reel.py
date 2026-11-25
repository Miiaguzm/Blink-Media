#!/usr/bin/env python3
"""
Arma un reel de anuncio (1080×1920) con fotos del artista y texto Blink encima.

Es la salida para cuando Mia no alcanza a grabarse: el reel se arma solo con
material que ya tenemos. Cada foto lleva un acercamiento lento —se pre-escala al
doble para que el zoom no la deje blanda— y los textos entran y salen con
fundidos. El logo prende con el titineo de la marca al principio, se queda
puesto, y se apaga con el mismo titineo al final.

Uso:
    python3 hacer-reel.py salida.mp4 --audio promo.mp4 \
        --bloque foto.png "PILDORA" "El titular de este bloque" \
        --bloque otra.png "" "Otro titular" ...
        [--cuenta @blinkmediacl] [--seg 5] [--crf 23]
"""

import argparse, json, os, shutil, subprocess, sys, tempfile, urllib.parse

AQUI = os.path.dirname(os.path.abspath(__file__))
PLANTILLA = os.path.join(AQUI, "reel-anuncio.html")
CHROMIUM = "/opt/pw-browsers/chromium"
ANCHO, ALTO = 1080, 1920
FPS = 30

# El mismo titineo de hacer-historia.py, para que las dos piezas se reconozcan.
ENTRA = [(0, 0.067), (0.133, 0.200), (0.233, 0.333)]
FIJO = 0.400
SALE = [(0.100, 0.167), (0.233, 0.300), (0.367, 0.433)]
FIN = 0.467


def correr(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("falló: " + " ".join(cmd[:4]) + "…\n" + (r.stderr or "")[-2000:])
    return r.stdout


def capa(carpeta, nombre, params):
    base = "file://" + urllib.parse.quote(PLANTILLA)
    crudo = os.path.join(carpeta, "crudo-%s.png" % nombre)
    correr([CHROMIUM, "-headless=new", "--no-sandbox", "--disable-gpu",
            "--hide-scrollbars", "--force-device-scale-factor=1",
            "--window-size=%d,%d" % (ANCHO, ALTO + 90),
            "--allow-file-access-from-files",
            "--default-background-color=00000000",
            "--virtual-time-budget=9000",
            "--screenshot=" + crudo,
            "%s?%s" % (base, urllib.parse.urlencode(params))])
    corte = os.path.join(carpeta, "%s.png" % nombre)
    correr(["ffmpeg", "-v", "error", "-i", crudo,
            "-vf", "crop=%d:%d:0:0" % (ANCHO, ALTO), corte, "-y"])
    return corte


def main():
    p = argparse.ArgumentParser()
    p.add_argument("salida")
    p.add_argument("--bloque", nargs=3, action="append", metavar=("FOTO", "PILDORA", "TITULAR"),
                   required=True, help="una foto, su píldora (vacía si no lleva) y su titular")
    p.add_argument("--audio", default=None, help="archivo del que se saca la música")
    p.add_argument("--cuenta", default="@blinkmediacl")
    p.add_argument("--seg", type=float, default=5.0, help="segundos por bloque")
    p.add_argument("--crf", default="23")
    a = p.parse_args()

    for f in (PLANTILLA, os.path.join(AQUI, "logo-blink.png")):
        if not os.path.exists(f):
            sys.exit("falta " + f)
    for b in a.bloque:
        if not os.path.exists(b[0]):
            sys.exit("falta la foto " + b[0])

    n = len(a.bloque)
    dur = a.seg * n
    print("bloques: %d · %.1f s cada uno · total %.1f s" % (n, a.seg, dur))

    carpeta = tempfile.mkdtemp(prefix="blink-reel-")
    try:
        velo = capa(carpeta, "velo", {"capa": "velo"})
        logo = capa(carpeta, "logo", {"capa": "logo"})
        textos = []
        for i, (foto, pil, tit) in enumerate(a.bloque):
            # La cuenta solo en el último bloque: repetirla en los cinco es ruido.
            params = {"capa": "texto", "pildora": pil, "titular": tit,
                      "cuenta": a.cuenta if i == n - 1 else ""}
            textos.append(capa(carpeta, "t%d" % i, params))

        cuadros = int(round(a.seg * FPS))
        entradas, filtros, etiquetas = [], [], []

        # ---- las fotos, cada una con su acercamiento ----
        for i, (foto, _, _) in enumerate(a.bloque):
            # La foto entra como UN solo cuadro y es zoompan el que produce los
            # d cuadros del bloque. Con -loop 1 -t N la entrada trae N×fps
            # cuadros y zoompan genera d por cada uno: el primer bloque se
            # estiraba sobre todo el reel y las demás fotos no aparecían nunca.
            entradas += ["-i", foto]
            filtros.append(
                "[{i}:v]scale=2160:3840:force_original_aspect_ratio=increase,"
                "crop=2160:3840,zoompan=z='min(zoom+0.0012,1.14)':d={d}:"
                "s={W}x{H}:fps={fps},setsar=1,format=rgba[f{i}]"
                .format(i=i, d=cuadros, W=ANCHO, H=ALTO, fps=FPS))
            etiquetas.append("[f%d]" % i)
        filtros.append("".join(etiquetas) + "concat=n=%d:v=1:a=0[base]" % n)

        # ---- el velo, puesto todo el reel ----
        iv = n
        entradas += ["-loop", "1", "-t", "%.3f" % (dur + 1), "-i", velo]
        filtros.append("[{i}:v]format=rgba,fade=t=in:st=0:d=0.5:alpha=1[velo]"
                       .format(i=iv))
        filtros.append("[base][velo]overlay=0:0[v0]")

        # ---- el logo: prende con el titineo, se queda, y se apaga igual ----
        il = n + 1
        entradas += ["-loop", "1", "-t", "%.3f" % (dur + 1), "-i", logo]
        sale = dur - FIN - 0.05
        tramos = [(a_, b_) for a_, b_ in ENTRA]
        tramos.append((FIJO, sale))
        tramos += [(sale + a_, sale + b_) for a_, b_ in SALE]
        gate = "+".join("between(t,%.3f,%.3f)" % t for t in tramos)
        filtros.append("[{i}:v]format=rgba[logo]".format(i=il))
        filtros.append("[v0][logo]overlay=0:0:enable='{g}'[v1]".format(g=gate))

        # ---- los textos, uno por bloque, con fundidos ----
        prev = "v1"
        for i, t in enumerate(textos):
            idx = n + 2 + i
            ini = i * a.seg
            entradas += ["-loop", "1", "-t", "%.3f" % (dur + 1), "-i", t]
            sig = "v%d" % (i + 2)

            if i == 0:
                # El primer texto prende con EL MISMO titineo del logo, en los
                # mismos cuadros. Mia me corrigió dos veces por escalonarlos: la
                # marca entra entera o no entra. Los textos del medio sí se
                # cruzan con fundidos, porque eso es cambiar de contenido y no
                # la entrada de la marca.
                g = "+".join("between(t,%.3f,%.3f)" % x for x in ENTRA)
                g += "+between(t,%.3f,%.3f)" % (FIJO, ini + a.seg - 0.35)
                filtros.append("[{idx}:v]format=rgba,fade=t=out:st={so}:d=0.35:alpha=1[x{i}]"
                               .format(idx=idx, so=ini + a.seg - 0.35, i=i))
                filtros.append("[{p}][x{i}]overlay=0:0:enable='{g}'[{s}]"
                               .format(p=prev, i=i, g=g, s=sig))
            elif i == n - 1:
                # Y el último se apaga con el titineo del logo, también a la vez.
                g = "between(t,%.3f,%.3f)" % (ini - 0.4, sale)
                g += "+" + "+".join("between(t,%.3f,%.3f)" % (sale + x[0], sale + x[1])
                                    for x in SALE)
                filtros.append("[{idx}:v]format=rgba,fade=t=in:st={si}:d=0.35:alpha=1[x{i}]"
                               .format(idx=idx, si=ini, i=i))
                filtros.append("[{p}][x{i}]overlay=0:0:enable='{g}'[{s}]"
                               .format(p=prev, i=i, g=g, s=sig))
            else:
                filtros.append(
                    "[{idx}:v]format=rgba,fade=t=in:st={si}:d=0.35:alpha=1,"
                    "fade=t=out:st={so}:d=0.35:alpha=1[x{i}]"
                    .format(idx=idx, si=ini, so=ini + a.seg - 0.35, i=i))
                filtros.append("[{p}][x{i}]overlay=0:0:enable='between(t,{a},{b})'[{s}]"
                               .format(p=prev, i=i, a=ini - 0.4,
                                       b=ini + a.seg + 0.1, s=sig))
            prev = sig

        cmd = ["ffmpeg", "-v", "error"] + entradas
        if a.audio:
            cmd += ["-t", "%.3f" % dur, "-i", a.audio]
        cmd += ["-filter_complex", ";".join(filtros), "-map", "[%s]" % prev]
        if a.audio:
            # La música se baja al final para que no quede cortada de golpe.
            cmd += ["-map", "%d:a" % (n + 2 + len(textos)),
                    "-af", "afade=t=out:st=%.2f:d=1.2" % (dur - 1.2),
                    "-c:a", "aac", "-b:a", "192k", "-ar", "48000"]
        else:
            cmd += ["-an"]
        cmd += ["-c:v", "libx264", "-preset", "slow", "-crf", a.crf,
                "-profile:v", "high", "-pix_fmt", "yuv420p",
                "-movflags", "+faststart", "-t", "%.3f" % dur, a.salida, "-y"]
        correr(cmd)
    finally:
        shutil.rmtree(carpeta, ignore_errors=True)

    s = json.loads(correr(["ffprobe", "-v", "error", "-print_format", "json",
                           "-show_streams", "-show_format", a.salida]))
    v = next(x for x in s["streams"] if x["codec_type"] == "video")
    hay = any(x["codec_type"] == "audio" for x in s["streams"])
    print("salida: %sx%s, %.1f s, audio: %s" %
          (v["width"], v["height"], float(s["format"]["duration"]), "sí" if hay else "no"))
    print("listo:", a.salida)


if __name__ == "__main__":
    main()
