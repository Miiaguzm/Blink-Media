
// ===== constantes (copiado tal cual del generador) =====
  const LOGO_B64 = "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";
  const ESTRELLA = "M 12.0 0.938 L 12.574 10.614 L 13.988 10.012 L 13.386 11.426 L 23.062 12.0 L 13.386 12.574 L 13.988 13.988 L 12.574 13.386 L 12.0 23.062 L 11.426 13.386 L 10.012 13.988 L 10.614 12.574 L 0.938 12.0 L 10.614 11.426 L 10.012 10.012 L 11.426 10.614 Z";
  const MORADO = "#7B2CFF", BLANCO = "#FFFFFF", NEGRO = "#0A0A0A";
  const W = 1080, H = 1350, MARGEN = 64, ANCHO_TEXTO = W - MARGEN * 2;

// ===== ayudas de texto (copiado tal cual del generador) =====
  function estrella(x, y, tamano, color, alpha){
    cx.save();
    cx.globalAlpha = alpha === undefined ? 1 : alpha;
    cx.fillStyle = color;
    cx.translate(x, y);
    cx.scale(tamano / 24, tamano / 24);
    cx.fill(new Path2D(ESTRELLA));
    cx.restore();
  }

  // Mismo mínimo que la plantilla: bajo 44px el titular deja de mandar.
  function ajustar(texto, base, maxAncho, familia){
    let t = base;
    cx.letterSpacing = "0.5px";
    while (t > 44){
      cx.font = t + "px " + familia;
      if (cx.measureText(texto).width <= maxAncho) break;
      t -= 1;
    }
    cx.letterSpacing = "0px";
    return t;
  }

  // Los textos libres (categoría, píldora, pie) pueden venir largos y no tienen
  // dónde cortarse: van en una sola línea. Se achica el cuerpo hasta que entren,
  // que es preferible a que se salgan del lienzo o pisen el logo.
  function encoger(texto, base, minimo, maxAncho, familia, peso, espaciado){
    let t = base;
    while (t > minimo){
      cx.font = peso + " " + t + "px " + familia;
      cx.letterSpacing = espaciado;
      if (cx.measureText(texto).width <= maxAncho) break;
      t -= 1;
    }
    return t;
  }

  function partir(texto, maxAncho){
    const palabras = texto.split(/\s+/).filter(Boolean);
    const lineas = [];
    let actual = "";
    for (const p of palabras){
      const prueba = actual ? actual + " " + p : p;
      if (cx.measureText(prueba).width > maxAncho && actual){
        lineas.push(actual); actual = p;
      } else { actual = prueba; }
    }
    if (actual) lineas.push(actual);
    return lineas;
  }

  // Reparte la bajada entre las líneas en vez de llenar la primera hasta el
  // tope: así la última palabra no queda sola abajo. Es lo mismo que hace
  // text-wrap:balance en la plantilla. Se van estrechando las líneas mientras
  // el texto siga cabiendo en la misma cantidad.
  function partirBalanceado(texto, maxAncho){
    const base = partir(texto, maxAncho);
    if (base.length < 2) return base;
    let mejor = base;
    for (let w = maxAncho - 8; w > maxAncho * 0.45; w -= 8){
      const p = partir(texto, w);
      if (p.length !== base.length) break;
      mejor = p;
    }
    return mejor;
  }

  // La caja de línea del navegador reparte el sobrante arriba y abajo del
  // texto. Sin esto el titular queda unos píxeles más alto que en la
  // plantilla y el bloque completo se corre.
  function lineaBase(topeCaja, altoCaja){
    const m = cx.measureText("Hg");
    const asc = m.fontBoundingBoxAscent, desc = m.fontBoundingBoxDescent;
    if (!asc) return topeCaja + altoCaja * 0.78;
    return topeCaja + (altoCaja - (asc + desc)) / 2 + asc;
  }

// ===== halo morado (copiado tal cual del generador) =====
  function haloMorado(cxx, x, y, rx, ry, alpha){
    cxx.save();
    cxx.globalCompositeOperation = "screen";
    cxx.translate(x, y);
    cxx.scale(1, ry / rx);
    const g = cxx.createRadialGradient(0, 0, 0, 0, 0, rx);
    g.addColorStop(0, "rgba(123,44,255," + alpha + ")");
    g.addColorStop(0.46, "rgba(123,44,255," + (alpha * 0.33).toFixed(3) + ")");
    g.addColorStop(0.72, "rgba(123,44,255,0)");
    g.addColorStop(1, "rgba(123,44,255,0)");
    cxx.fillStyle = g;
    cxx.beginPath(); cxx.arc(0, 0, rx, 0, Math.PI * 2); cxx.fill();
    cxx.restore();
  }

// ===== fondo desenfocado (copiado tal cual del generador) =====
  function medidas(src){
    return { w: src.videoWidth || src.width, h: src.videoHeight || src.height };
  }

  // ¿El navegador sabe hacer desenfoque de verdad? Safari no lo trajo hasta el
  // 17.4, así que se prueba una vez: si al asignar el filtro el valor no queda
  // guardado, no hay soporte y se usa el camino de abajo.
  const HAY_FILTRO = (function(){
    try {
      const c = document.createElement("canvas").getContext("2d");
      c.filter = "blur(2px)";
      return c.filter === "blur(2px)";
    } catch (e) { return false; }
  })();

  // Lienzos que se reutilizan: en un video esto corre en cada cuadro y crear uno
  // nuevo cada vez es caro.
  const lienzoA = document.createElement("canvas");
  const lienzoB = document.createElement("canvas");
  const lienzoC = document.createElement("canvas");

  // Suavizado para navegadores sin filtros: en vez de un salto brusco, baja y
  // sube de a mitades. Cada pasada interpola, y varias seguidas se parecen a un
  // gaussiano sin dejar los cuadrados que deja un solo salto grande.
  function suavizarPorMitades(origen, aw, ah, radio){
    const pasos = Math.max(1, Math.min(4, Math.round(Math.log2(Math.max(2, radio)))));
    let w = aw, h = ah, desde = origen;
    const mover = (nw, nh) => {
      const destino = (desde === lienzoB) ? lienzoC : lienzoB;
      if (destino.width !== nw || destino.height !== nh){
        destino.width = nw; destino.height = nh;
      }
      const c = destino.getContext("2d");
      c.imageSmoothingEnabled = true;
      c.imageSmoothingQuality = "high";
      c.clearRect(0, 0, nw, nh);
      c.drawImage(desde, 0, 0, w, h, 0, 0, nw, nh);
      desde = destino; w = nw; h = nh;
    };
    for (let i = 0; i < pasos; i++) mover(Math.max(8, w >> 1), Math.max(8, h >> 1));
    for (let i = 0; i < pasos; i++) mover(Math.min(aw, w * 2), Math.min(ah, h * 2));
    return desde;
  }

  // El fondo desenfocado tiene dos partes. Antes era una sola: achicar muchísimo
  // la imagen y volver a estirarla. Con el control al máximo eso la dejaba en
  // unos 47px de ancho, y al estirarla a 1080 se veían los cuadrados. Ahora se
  // achica poco —solo para que salga barato— y el suavizado de verdad lo hace un
  // desenfoque gaussiano encima, que no pixela por mucho que se suba el control.
  function fondoBorroso(img, ancho, alto, desenfoque, brillo){
    const m = medidas(img);
    if (!m.w || !m.h) return;
    const desborde = Math.max(120, desenfoque * 8);
    const bw = ancho + desborde * 2, bh = alto + desborde * 2;

    const reduccion = desenfoque > 0 ? Math.min(6, 1 + desenfoque * 0.25) : 1;
    const aw = Math.max(32, Math.round(bw / reduccion));
    const ah = Math.max(32, Math.round(bh / reduccion));

    // Asignar width a un canvas lo reconstruye entero. En un video eso pasaba
    // 30 veces por segundo sin necesidad: durante una grabación el tamaño no
    // cambia nunca.
    if (lienzoA.width !== aw || lienzoA.height !== ah){
      lienzoA.width = aw; lienzoA.height = ah;
    }
    const ca = lienzoA.getContext("2d");
    ca.imageSmoothingEnabled = true;
    ca.imageSmoothingQuality = "high";

    const esc = Math.max(aw / m.w, ah / m.h);
    const dw = m.w * esc, dh = m.h * esc;
    ca.clearRect(0, 0, aw, ah);
    ca.drawImage(img, (aw - dw) / 2, (ah - dh) / 2, dw, dh);

    // El brillo y la desaturación se aplican sobre el lienzo chico, que por su
    // tamaño sale gratis.
    try {
      const d = ca.getImageData(0, 0, aw, ah), q = d.data;
      for (let i = 0; i < q.length; i += 4){
        let r = q[i], g = q[i + 1], b = q[i + 2];
        const gris = 0.299 * r + 0.587 * g + 0.114 * b;
        r += (gris - r) * 0.20; g += (gris - g) * 0.20; b += (gris - b) * 0.20;
        q[i]     = Math.min(255, r * brillo);
        q[i + 1] = Math.min(255, g * brillo);
        q[i + 2] = Math.min(255, b * brillo);
      }
      ca.putImageData(d, 0, 0);
    } catch (e) { /* sin ajuste de color antes que sin fondo */ }

    cx.imageSmoothingEnabled = true;
    cx.imageSmoothingQuality = "high";

    if (desenfoque <= 0){
      cx.drawImage(lienzoA, -desborde, -desborde, bw, bh);
      return;
    }

    // El radio se calcula para que el control se sienta igual que antes: el
    // desenfoque total queda parecido, pero repartido de otra forma.
    const radio = desenfoque * 0.6;

    if (HAY_FILTRO){
      cx.save();
      cx.filter = "blur(" + radio.toFixed(1) + "px)";
      cx.drawImage(lienzoA, -desborde, -desborde, bw, bh);
      cx.restore();
      return;
    }

    cx.drawImage(suavizarPorMitades(lienzoA, aw, ah, radio), -desborde, -desborde, bw, bh);
  }

// ===== lamina (copiado tal cual del generador) =====
  const LW = 1080, LH = 1350, LMAR = 72, ANCHO_L = LW - LMAR * 2;
  const TOPE_L = 195;

  function dibujarLamina(){
    cx.clearRect(0, 0, LW, LH);
    cx.fillStyle = NEGRO;
    cx.fillRect(0, 0, LW, LH);

    const desenfoque = parseFloat($("l-desenfoque").value);
    const brillo = parseFloat($("l-brillo").value);
    const fuente = videoLamina || imgLamina;

    // ---- fondo: la misma imagen, o una foto aparte ----
    // Con "otra" y sin foto cargada todavía se sigue usando la misma imagen,
    // para que la lámina nunca quede sin fondo mientras ella elige el archivo.
    const fondo = ($("l-fondotipo").value === "otra" && fondoLamina) ? fondoLamina : fuente;
    if (fondo){
      fondoBorroso(fondo, LW, LH, desenfoque, brillo);

      const v = cx.createLinearGradient(0, 0, 0, LH);
      v.addColorStop(0, "rgba(10,10,10,0.80)");
      v.addColorStop(0.22, "rgba(10,10,10,0.66)");
      v.addColorStop(0.50, "rgba(10,10,10,0.58)");
      v.addColorStop(0.78, "rgba(10,10,10,0.70)");
      v.addColorStop(1, "rgba(10,10,10,0.88)");
      cx.fillStyle = v; cx.fillRect(0, 0, LW, LH);
    } else {
      const g = cx.createRadialGradient(LW / 2, LH * 0.15, 40, LW / 2, LH * 0.15, LW * 1.1);
      g.addColorStop(0, "rgba(123,44,255,0.45)");
      g.addColorStop(1, "rgba(10,10,10,0)");
      cx.fillStyle = g; cx.fillRect(0, 0, LW, LH);
    }

    // ---- halo abajo y destello ----
    haloMorado(cx, LW / 2, LH + 200 - 420, 620, 420, 0.38);
    estrella(LW - 560 + 120, 120, 560, MORADO, 0.14);

    // ---- logo arriba a la derecha, igual que en el carrusel ----
    if (logo.complete && logo.naturalWidth){
      const alto = 152, ancho = logo.naturalWidth * (alto / logo.naturalHeight);
      cx.drawImage(logo, LW - 64 - ancho, 28, ancho, alto);
    }

    // ---- bloque imagen + línea ----
    const texto = $("l-texto").value.trim();
    cx.font = "600 33px Montserrat, sans-serif";
    const lineasT = texto ? partirBalanceado(texto, 880) : [];
    const altoT = lineasT.length * 47.9;
    const gap = altoT ? 34 : 0;

    const disponible = LH - TOPE_L - 70;

    // El control de tamaño es una fracción de LO MÁS GRANDE QUE CABE, no del
    // ancho de la lámina. Antes se calculaba sobre el ancho y después se
    // recortaba para que entrara: con una foto vertical ese recorte se comía
    // todo el tramo de arriba del control y moverlo no cambiaba nada. Midiendo
    // primero el calce —por ancho o por alto, el que apriete— el 100% es
    // siempre "lo más grande posible" y el control responde en todo su rango,
    // sea la imagen cuadrada, apaisada o vertical.
    let anchoImg = 0, altoImg = 0;
    if (fuente){
      const m = medidas(fuente);
      const altoLibre = disponible - gap - altoT;
      if (m.w && m.h && altoLibre > 0){
        const calce = Math.min(ANCHO_L / m.w, altoLibre / m.h);
        const tam = parseFloat($("l-tam").value) / 100;
        anchoImg = m.w * calce * tam;
        altoImg  = m.h * calce * tam;
      }
    }
    const total = altoImg + gap + altoT;

    let y = TOPE_L + Math.max(0, (disponible - total) / 2);
    const centro = LW / 2;

    if (altoImg){
      const x = centro - anchoImg / 2;
      cx.save();
      cx.beginPath(); cx.roundRect(x, y, anchoImg, altoImg, 24); cx.clip();
      cx.drawImage(fuente, x, y, anchoImg, altoImg);
      cx.restore();
      cx.beginPath(); cx.roundRect(x, y, anchoImg, altoImg, 24);
      cx.lineWidth = 1.5; cx.strokeStyle = "rgba(255,255,255,0.16)"; cx.stroke();
      y += altoImg + gap;
    }

    if (lineasT.length){
      cx.textAlign = "center";
      cx.font = "600 33px Montserrat, sans-serif";
      cx.fillStyle = "rgba(255,255,255,0.90)";
      lineasT.forEach((linea, i) => {
        cx.fillText(linea, centro, lineaBase(y + i * 47.9, 47.9));
      });
      cx.textAlign = "left";
    }
  }

// ===== portada (copiado tal cual del generador) =====
  function dibujar(){
    cx.clearRect(0, 0, W, H);
    cx.fillStyle = NEGRO;
    cx.fillRect(0, 0, W, H);

    const clara = $("clara").checked;

    // ---- foto o video ----
    // Un video se mide con videoWidth, no con width, que en un <video> es el
    // ancho del elemento en pantalla y no el del archivo.
    const medio = videoPortada || foto;
    if (medio){
      const m = medidas(medio);
      const zoom = parseFloat($("zoom").value);
      const pos = parseFloat($("pos").value) / 100;
      const posX = parseFloat($("posx").value) / 100;
      const brillo = parseFloat($("brillo").value);
      const escala = Math.max(W / m.w, H / m.h) * zoom;
      const dw = m.w * escala, dh = m.h * escala;
      cx.save();
      cx.filter = "grayscale(12%) contrast(1.08) brightness(" + brillo + ") saturate(1.05)";
      cx.drawImage(medio, (W - dw) * posX, (H - dh) * pos, dw, dh);
      cx.restore();
    } else {
      const g = cx.createRadialGradient(W/2, H*0.18, 40, W/2, H*0.18, W*0.95);
      g.addColorStop(0, "rgba(123,44,255,0.5)");
      g.addColorStop(1, "rgba(10,10,10,0)");
      cx.fillStyle = g; cx.fillRect(0, 0, W, H);
    }

    // ---- velo ----
    const v = cx.createLinearGradient(0, 0, 0, H);
    if (clara){
      v.addColorStop(0, "rgba(10,10,10,0.86)");
      v.addColorStop(0.20, "rgba(10,10,10,0.46)");
      v.addColorStop(0.44, "rgba(10,10,10,0.40)");
      v.addColorStop(0.66, "rgba(10,10,10,0.86)");
      v.addColorStop(0.85, "rgba(10,10,10,0.98)");
    } else {
      v.addColorStop(0, "rgba(10,10,10,0.55)");
      v.addColorStop(0.18, "rgba(10,10,10,0.05)");
      v.addColorStop(0.42, "rgba(10,10,10,0.10)");
      v.addColorStop(0.66, "rgba(10,10,10,0.78)");
      v.addColorStop(0.85, "rgba(10,10,10,0.97)");
    }
    v.addColorStop(1, NEGRO);
    cx.fillStyle = v; cx.fillRect(0, 0, W, H);

    // ---- halo morado ----
    // Elipse de 1100x600 centrada 140px por debajo del borde inferior, en modo
    // screen: es el halo que le da profundidad al fondo detrás del titular.
    cx.save();
    cx.globalCompositeOperation = "screen";
    cx.translate(W / 2, H + 140 - 300);
    cx.scale(1, 300 / 550);
    const halo = cx.createRadialGradient(0, 0, 0, 0, 0, 550);
    halo.addColorStop(0, "rgba(123,44,255,0.30)");
    halo.addColorStop(0.65, "rgba(123,44,255,0)");
    halo.addColorStop(1, "rgba(123,44,255,0)");
    cx.fillStyle = halo;
    cx.beginPath(); cx.arc(0, 0, 550, 0, Math.PI * 2); cx.fill();
    cx.restore();

    // ---- encabezado ----
    let anchoLogo = 0;
    if (logo.complete && logo.naturalWidth){
      const alto = 152;
      anchoLogo = logo.naturalWidth * (alto / logo.naturalHeight);
      cx.drawImage(logo, W - MARGEN - anchoLogo, 28, anchoLogo, alto);
    }

    estrella(MARGEN, 78, 56, MORADO);
    const cat = $("categoria").value.toUpperCase();
    // La categoría no puede llegar a tocar el logo.
    const espacioCat = (W - MARGEN - anchoLogo - 24) - (MARGEN + 70);
    const tCat = encoger(cat, 26, 15, espacioCat, "Montserrat, sans-serif", "800", "2px");
    cx.fillStyle = MORADO;
    cx.font = "800 " + tCat + "px Montserrat, sans-serif";
    cx.textBaseline = "middle";
    cx.letterSpacing = "2px";
    cx.fillText(cat, MARGEN + 70, 107);
    cx.letterSpacing = "0.5px";
    cx.fillStyle = "rgba(255,255,255,0.85)";
    cx.font = "500 29px Montserrat, sans-serif";
    cx.fillText($("fecha").value, MARGEN + 70, 160);
    cx.letterSpacing = "0px";
    cx.textBaseline = "alphabetic";

    // ---- medidas del bloque de texto ----
    const bajada = $("bajada").value.trim();
    // La bajada va en negrita (700). Tiene que medirse con el mismo peso con el
    // que se dibuja: la negrita es más ancha y si se mide en 400 las líneas se
    // pasan del ancho al pintarlas.
    cx.font = "700 30px Montserrat, sans-serif";
    const lineasBajada = bajada ? partirBalanceado(bajada, 880) : [];
    const altoBajada = lineasBajada.length * 42.6;

    const fondoBloque = H - (bajada ? 215 : 300);
    const topeBajada = fondoBloque - altoBajada;
    const fondoTitular = bajada ? topeBajada - 28 : fondoBloque;

    const l1 = $("linea1").value.toUpperCase();
    const l2 = $("linea2").value.toUpperCase();
    // Las dos líneas comparten cuerpo, como en el carrusel: se busca el mayor
    // tamaño con el que quepan las dos. Ajustándolas por separado, la corta se
    // quedaba grande y la larga achicada.
    const a1 = l1 ? ajustar(l1, 132, ANCHO_TEXTO, "Anton, sans-serif") : 0;
    const a2 = l2 ? ajustar(l2, 132, ANCHO_TEXTO, "Anton, sans-serif") : 0;
    const cuerpo = (a1 && a2) ? Math.min(a1, a2) : (a1 || a2);
    const t1 = l1 ? cuerpo : 0, t2 = l2 ? cuerpo : 0;
    const caja1 = t1 * 1.2, caja2 = t2 * 1.2;
    const topeTitular = fondoTitular - caja1 - caja2;

    // ---- destello sobre el titular ----
    estrella(W - MARGEN - 150, topeTitular - 172, 150, MORADO, 0.9);

    // ---- píldora ----
    const pil = $("pildora").value.toUpperCase();
    if (pil){
      const tPil = encoger(pil, 24, 15, ANCHO_TEXTO - 52, "Montserrat, sans-serif", "700", "1.5px");
      cx.font = "700 " + tPil + "px Montserrat, sans-serif";
      cx.letterSpacing = "1.5px";
      const anchoTexto = cx.measureText(pil).width;
      const ancho = anchoTexto + 52, alto = 53;
      const y = topeTitular - 26 - alto;
      cx.beginPath();
      cx.roundRect(MARGEN, y, ancho, alto, alto / 2);
      cx.fillStyle = "rgba(10,10,10,0.55)"; cx.fill();
      cx.lineWidth = 1.5; cx.strokeStyle = "rgba(255,255,255,0.7)"; cx.stroke();
      cx.fillStyle = BLANCO;
      cx.textBaseline = "middle";
      cx.fillText(pil, MARGEN + 26, y + alto / 2 + 1);
      cx.textBaseline = "alphabetic";
      cx.letterSpacing = "0px";
    }

    // ---- titular ----
    cx.letterSpacing = "0.5px";
    if (l1){
      cx.font = t1 + "px Anton, sans-serif";
      cx.fillStyle = BLANCO;
      cx.fillText(l1, MARGEN, lineaBase(topeTitular, caja1));
    }
    if (l2){
      cx.font = t2 + "px Anton, sans-serif";
      cx.fillStyle = MORADO;
      cx.fillText(l2, MARGEN, lineaBase(topeTitular + caja1, caja2));
    }
    cx.letterSpacing = "0px";

    // ---- bajada ----
    if (lineasBajada.length){
      cx.font = "700 30px Montserrat, sans-serif";
      cx.fillStyle = "rgba(255,255,255,0.92)";
      lineasBajada.forEach((linea, i) => {
        cx.fillText(linea, MARGEN, lineaBase(topeBajada + i * 42.6, 42.6));
      });
    }

    // ---- pie ----
    const pie = $("pie").value.toUpperCase();
    cx.strokeStyle = "rgba(255,255,255,0.18)"; cx.lineWidth = 1.5;
    cx.beginPath(); cx.moveTo(0, H - 128); cx.lineTo(W, H - 128); cx.stroke();

    const tPie = encoger(pie, 24, 14, W - MARGEN * 2 - 50, "Montserrat, sans-serif", "700", "1.5px");
    cx.font = "700 " + tPie + "px Montserrat, sans-serif";
    cx.letterSpacing = "1.5px";
    const anchoPie = cx.measureText(pie).width;
    const total = anchoPie + 50;
    const inicio = (W - total) / 2;
    // Centro de la fila del pie: 56px de margen inferior y 36px de alto útil.
    const cy = H - 74;

    cx.strokeStyle = MORADO; cx.lineWidth = 3;
    cx.lineCap = "round"; cx.lineJoin = "round";
    cx.beginPath();
    cx.moveTo(inicio, cy); cx.lineTo(inicio + 30, cy);
    cx.moveTo(inicio + 19, cy - 11); cx.lineTo(inicio + 30, cy); cx.lineTo(inicio + 19, cy + 11);
    cx.stroke();

    cx.fillStyle = BLANCO;
    cx.textBaseline = "middle";
    cx.fillText(pie, inicio + 50, cy + 1);
    cx.textBaseline = "alphabetic";
    cx.letterSpacing = "0px";
  }
