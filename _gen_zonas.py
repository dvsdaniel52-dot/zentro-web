#!/usr/bin/env python3
"""Genera las páginas por zona (SEO local): gym cerca de Interlomas, La Herradura y en Huixquilucan.
Toma el diseño (estilos, menú, pie y botón de WhatsApp) de hyrox-bosque-real/index.html. Correr: python _gen_zonas.py"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
BASE = open(os.path.join(AQUI, "hyrox-bosque-real", "index.html"), encoding="utf-8").read()
ESTILO = BASE[BASE.index("<style>"):BASE.index("</style>") + len("</style>")]
MENU = BASE[BASE.index('<header class="nav">'):BASE.index("</header>") + len("</header>")]
PIE = BASE[BASE.index("</main>") + len("</main>"):]

GYM = {"@type": "ExerciseGym", "@id": "https://zentrocf.com/#gym", "name": "Zentro Community Fitness",
       "url": "https://zentrocf.com/", "telephone": "+52 55 8541 8713",
       "address": {"@type": "PostalAddress", "streetAddress": "Blvd. Bosque Real 85, Plaza Trípode, Piso R",
                   "addressLocality": "Huixquilucan", "addressRegion": "Estado de México", "postalCode": "52774",
                   "addressCountry": "MX"}}

ZONAS = [
    {"slug": "gym-interlomas", "zona": "Interlomas", "h1a": "Gym cerca", "h1b": "de Interlomas",
     "title": "Gym cerca de Interlomas | Functional, HYROX y Calistenia | Zentro",
     "desc": "Gym boutique a unos minutos de Interlomas, dentro de Bosque Real: Functional Training, HYROX, Calistenia y Booty Camp con coach, en grupos chicos. InBody y clase muestra sin costo.",
     "sub": "Si vives o trabajas en Interlomas, Zentro te queda a la vuelta: estamos dentro de Bosque Real, en Plaza Trípode. Clases en grupos chicos, con un coach que sabe tu nombre y te corrige la técnica.",
     "llegar": "Desde Interlomas llegas por el Blvd. Bosque Real. Plaza Trípode está junto al Hospital NOOR, frente a la glorieta roja. Zentro está en el Piso R.",
     "faq": [("¿Zentro está en Interlomas?", "No: estamos dentro de Bosque Real, en Plaza Trípode (Blvd. Bosque Real 85), a unos minutos de Interlomas. Muchos de nuestros socios viven o trabajan en Interlomas."),
             ("¿A qué hora puedo entrenar si trabajo en Interlomas?", "Hay clases desde las 5:40 de la mañana y hasta las 19:20 de lunes a viernes, y el sábado a las 7:30 y 9:00. Puedes venir antes o después de la oficina."),
             ("¿Dónde me estaciono?", "En el valet de Plaza Trípode. Dile que vienes a Zentro y no pagas estacionamiento.")]},
    {"slug": "gym-la-herradura", "zona": "La Herradura", "h1a": "Gym cerca", "h1b": "de La Herradura",
     "title": "Gym cerca de La Herradura | Clases con coach en Bosque Real | Zentro",
     "desc": "Gym boutique cerca de La Herradura, dentro de Bosque Real: Functional Training, HYROX, Calistenia y Booty Camp con coach, en grupos chicos. InBody y clase muestra sin costo.",
     "sub": "Si vives en La Herradura, tienes un gym con coach muy cerca: Zentro está dentro de Bosque Real, en Plaza Trípode. Entrenas en grupos chicos, a tu nivel, y mides tu avance con InBody.",
     "llegar": "Desde La Herradura llegas por el Blvd. Bosque Real. Plaza Trípode está junto al Hospital NOOR, frente a la glorieta roja. Zentro está en el Piso R.",
     "faq": [("¿Zentro está en La Herradura?", "No: estamos dentro de Bosque Real, en Plaza Trípode (Blvd. Bosque Real 85), muy cerca de La Herradura."),
             ("¿Necesito experiencia?", "No. Las clases son para cualquier nivel: el coach ajusta cargas y ejercicios a ti desde el primer día."),
             ("¿Dónde me estaciono?", "En el valet de Plaza Trípode. Dile que vienes a Zentro y no pagas estacionamiento.")]},
    {"slug": "gym-huixquilucan", "zona": "Huixquilucan", "h1a": "Gym en", "h1b": "Huixquilucan",
     "title": "Gym en Huixquilucan | Bosque Real · Clases con coach | Zentro",
     "desc": "Gym boutique en Huixquilucan, dentro de Bosque Real: Functional Training, HYROX, Calistenia y Booty Camp con coach, en grupos chicos. InBody y clase muestra sin costo.",
     "sub": "Zentro es un gym boutique en Huixquilucan, dentro de Bosque Real. Clases en grupos chicos de Functional Training, HYROX, Calistenia y Booty Camp, con coach y con tu avance medido en InBody.",
     "llegar": "Estamos en Blvd. Bosque Real 85, Plaza Trípode, Piso R, dentro de Bosque Real (Huixquilucan). Plaza Trípode está junto al Hospital NOOR, frente a la glorieta roja.",
     "faq": [("¿En qué parte de Huixquilucan está Zentro?", "Dentro de Bosque Real, en Plaza Trípode (Blvd. Bosque Real 85, Piso R), junto al Hospital NOOR. Queda cerca de Interlomas, La Herradura y Tecamachalco."),
             ("¿Qué clases hay?", "Functional Training (la clase base), HYROX, Calistenia y Booty Camp. Todas con coach y en grupos chicos."),
             ("¿Dónde me estaciono?", "En el valet de Plaza Trípode. Dile que vienes a Zentro y no pagas estacionamiento.")]},
]
FAQ_COMUN = [("¿Cómo empiezo?", "Con tu InBody gratis (unos 20 minutos) o con una clase muestra sin costo. Los dos se agendan en un minuto en la App Zentro, sin crear cuenta.")]


def pagina(z):
    url = f"https://zentrocf.com/{z['slug']}/"
    faqs = z["faq"] + FAQ_COMUN
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": z["title"], "description": z["desc"], "url": url, "about": GYM},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://zentrocf.com/"},
            {"@type": "ListItem", "position": 2, "name": f"{z['h1a']} {z['h1b']}", "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]}
    faq_html = "\n".join(f"      <details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{z['title']}</title>
<meta name="description" content="{z['desc']}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{z['title']}">
<meta property="og:description" content="{z['desc']}">
<meta property="og:image" content="https://zentrocf.com/img/portada.jpg">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#1B2227">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/img/icon-512.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Playfair+Display:ital@0;1&display=swap">
{ESTILO}
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
</script>
</head>
<body>
{MENU}

<main>
<section class="hero">
  <div class="inner hero-grid">
    <div>
      <p class="crumbs"><a href="/">Inicio</a> / {z['zona']}</p>
      <h1><span class="where">Gym en Bosque Real · Plaza Trípode</span><span class="a">{z['h1a']}</span><span class="b">{z['h1b']}</span></h1>
      <p class="sub">{z['sub']}</p>
      <div class="ctas">
        <a class="btn solid" href="https://app.zentrocf.com/agenda/inbody" target="_blank" rel="noopener">Agenda tu InBody gratis</a>
        <a class="btn line" href="https://app.zentrocf.com/agenda/clase-muestra" target="_blank" rel="noopener">Toma una clase muestra</a>
      </div>
      <p class="micro">El InBody y la clase muestra no cuestan nada.</p>
    </div>
    <figure class="hero-fig"><img src="/img/portada.jpg" alt="Clase en Zentro Community Fitness, gym en Bosque Real" loading="eager"></figure>
  </div>
</section>

<section class="piedra">
  <div class="inner">
    <p class="label">Qué entrenas</p>
    <h2>Cuatro clases,<em>un coach contigo</em></h2>
    <p class="lede">Todas las clases son en grupos chicos y para cualquier nivel. Empiezas con tu InBody para saber tu punto de partida y lo repetimos a las 6 semanas.</p>
    <nav class="others" aria-label="Clases">
        <a href="/entrenamiento-funcional-bosque-real/">Functional Training</a>
        <a href="/hyrox-bosque-real/">HYROX</a>
        <a href="/calistenia-bosque-real/">Calistenia</a>
        <a href="/booty-camp-bosque-real/">Booty Camp</a>
        <a href="/inbody-gratis/">InBody gratis</a>
    </nav>
  </div>
</section>

<section>
  <div class="inner">
    <div class="two">
      <div>
        <p class="label">Horario</p>
        <h2>Antes o después<em>de tu día</em></h2>
        <table class="hours" aria-label="Horario" style="margin-top:30px">
        <tr><td>Functional Training</td><td>L-V 6:00 · 7:15 · 8:30 · 9:45 · 17:00 · 19:20<br>Sáb 7:30 · 9:00</td></tr>
        <tr><td>HYROX</td><td>L-V 5:40 · 8:00 · 18:10</td></tr>
        <tr><td>Calistenia</td><td>Lun, mié y vie 7:00 · 9:00</td></tr>
        <tr><td>Booty Camp</td><td>Mar y jue 7:00 · 9:00</td></tr>
        </table>
      </div>
      <div>
        <p class="label">Cómo llegar</p>
        <h2>Plaza Trípode<em>dentro de Bosque Real</em></h2>
        <p class="lede">{z['llegar']} Dile al valet que vienes a Zentro y no pagas estacionamiento.</p>
        <div class="ctas"><a class="btn solid" href="https://www.google.com/maps/search/?api=1&query=Zentro+Community+Fitness+Bosque+Real" target="_blank" rel="noopener">Abrir en Google Maps</a><a class="btn line" href="https://wa.me/525585418713" target="_blank" rel="noopener">WhatsApp</a></div>
      </div>
    </div>
  </div>
</section>

<section class="piedra">
  <div class="inner">
    <p class="label">Preguntas frecuentes</p>
    <h2>Antes de venir</h2>
    <div class="faq">
{faq_html}
    </div>
  </div>
</section>

<section>
  <div class="inner two" style="margin-top:0">
    <div>
      <p class="label">Contacto</p>
      <h2>Zentro Community<em>Fitness</em></h2>
    </div>
    <div class="contact">
      <p><small>Dirección</small>Blvd. Bosque Real 85, Plaza Trípode, Piso R, Bosque Real, Huixquilucan, Edo. de México, 52774</p>
      <p><small>Cerca de</small>Interlomas, La Herradura, Tecamachalco y Huixquilucan</p>
      <p><small>Teléfono y WhatsApp</small>55 8541 8713</p>
    </div>
  </div>
</section>
</main>{PIE}"""


for z in ZONAS:
    os.makedirs(os.path.join(AQUI, z["slug"]), exist_ok=True)
    open(os.path.join(AQUI, z["slug"], "index.html"), "w", encoding="utf-8", newline="\n").write(pagina(z))
    print("ok", z["slug"])
