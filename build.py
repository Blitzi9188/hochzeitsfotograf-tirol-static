# -*- coding: utf-8 -*-
import os

OUT = os.path.dirname(os.path.abspath(__file__))
B = "https://hochzeitsfotograf.tirol/assets/uploads/"

USED = set()
def img(name):
    USED.add(name)
    return "assets/img/" + name  # local path; site.js falls back to the live URL if missing

# ---------- HEAD ----------
def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="de" data-lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<script>document.documentElement.classList.add('js');</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Jost:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>'''

# ---------- HEADER ----------
NAV = [
    ("standesamt.html", "Standesamt", "Registry office", "service"),
    ("familie.html", "Familienfotografie", "Family", "service"),
    ("paar-portraet.html", "Paar & Porträt", "Couple & portrait", "service"),
]
def header(active):
    def acls(href): return ' class="active"' if active==href else ''
    return f'''
<header class="hdr" id="hdr">
  <div class="wrap-wide hdr-inner">
    <a href="index.html" class="brand" aria-label="Andreas Kiss — Startseite">
      <span class="brand-name">ANDREAS&nbsp;KISS</span>
      <span class="brand-sub de">Hochzeitsfotografie · Innsbruck</span>
      <span class="brand-sub en">Wedding Photography · Innsbruck</span>
    </a>
    <nav class="mainnav" aria-label="Hauptmenü">
      <a href="standesamt.html"{acls('standesamt.html')}><span class="de">Standesamt</span><span class="en">Registry office</span></a>
      <a href="familie.html"{acls('familie.html')}><span class="de">Familie</span><span class="en">Family</span></a>
      <a href="paar-portraet.html"{acls('paar-portraet.html')}><span class="de">Paar &amp; Porträt</span><span class="en">Couple &amp; portrait</span></a>
      <a href="portfolio.html"{acls('portfolio.html')}>Portfolio</a>
      <a href="guide.html"{acls('guide.html')}>Guide</a>
      <a href="preise.html"{acls('preise.html')}><span class="de">Preise</span><span class="en">Pricing</span></a>
      <a href="ueber-mich.html"{acls('ueber-mich.html')}><span class="de">Über mich</span><span class="en">About</span></a>
      <a href="kontakt.html"{acls('kontakt.html')}><span class="de">Kontakt</span><span class="en">Contact</span></a>
    </nav>
    <div class="hdr-right">
      <div class="lang" role="group" aria-label="Sprache / Language">
        <button type="button" data-set-lang="de" aria-pressed="true">DE</button><span class="sep">/</span><button type="button" data-set-lang="en" aria-pressed="false">EN</button>
      </div>
      <a href="kontakt.html" class="btn btn-primary btn-sm"><span class="de">Anfragen</span><span class="en">Enquire</span></a>
      <button class="burger" id="burger" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="mobilenav" id="mobilenav" data-open="false" aria-label="Menü">
  <a href="standesamt.html"><span class="de">Standesamt &amp; kleine Hochzeiten</span><span class="en">Registry &amp; small weddings</span></a>
  <a href="familie.html"><span class="de">Familienfotografie</span><span class="en">Family photography</span></a>
  <a href="paar-portraet.html"><span class="de">Paar &amp; Porträt</span><span class="en">Couple &amp; portrait</span></a>
  <a href="portfolio.html">Portfolio</a>
  <a href="guide.html">Guide</a>
  <a href="preise.html"><span class="de">Preise</span><span class="en">Pricing</span></a>
  <a href="ueber-mich.html"><span class="de">Über mich</span><span class="en">About</span></a>
  <a href="kontakt.html"><span class="de">Kontakt</span><span class="en">Contact</span></a>
  <div class="mlang" role="group" aria-label="Sprache">
    <button type="button" data-set-lang="de" aria-pressed="true">Deutsch</button>
    <button type="button" data-set-lang="en" aria-pressed="false">English</button>
  </div>
</nav>'''

# ---------- CTA + FOOTER ----------
def cta():
    return '''
<section class="section cta">
  <div class="wrap reveal">
    <p class="kicker centered on-dark"><span class="de">Anfrage</span><span class="en">Enquiry</span></p>
    <h2 class="h-lg" style="margin-top:1.3rem;"><span class="de">Erzählt mir von euch und eurem Tag.</span><span class="en">Tell me about you and your day.</span></h2>
    <p><span class="de">Standesamt, kleine Hochzeit, Familie oder Porträt – schreibt mir kurz, worum es geht. Ich antworte innerhalb von zwei Werktagen.</span><span class="en">Registry office, small wedding, family or portrait – tell me briefly what it's about. I reply within two working days.</span></p>
    <a href="kontakt.html" class="btn btn-primary btn-lg"><span class="de">Termin anfragen</span><span class="en">Enquire now</span></a>
  </div>
</section>'''

def footer():
    return '''
<footer class="footer">
  <div class="wrap-wide">
    <div class="top">
      <div>
        <span class="brand-name">ANDREAS KISS</span>
        <p class="fbio"><span class="de">Hochzeits-, Familien- und Porträtfotografie in Innsbruck und ganz Tirol. Ruhig, ehrlich, ohne Inszenierung.</span><span class="en">Wedding, family and portrait photography in Innsbruck and across Tyrol. Calm, honest, unstaged.</span></p>
      </div>
      <div>
        <h5><span class="de">Seiten</span><span class="en">Pages</span></h5>
        <ul>
          <li><a href="standesamt.html"><span class="de">Standesamt Innsbruck</span><span class="en">Registry office</span></a></li>
          <li><a href="familie.html"><span class="de">Familienfotografie</span><span class="en">Family</span></a></li>
          <li><a href="paar-portraet.html"><span class="de">Paar &amp; Porträt</span><span class="en">Couple &amp; portrait</span></a></li>
          <li><a href="preise.html"><span class="de">Preise &amp; Pakete</span><span class="en">Pricing</span></a></li>
          <li><a href="guide.html"><span class="de">Guide (Tirol)</span><span class="en">Guide (Tyrol)</span></a></li>
          <li><a href="portfolio.html">Portfolio</a></li>
          <li><a href="ueber-mich.html"><span class="de">Über mich</span><span class="en">About</span></a></li>
        </ul>
      </div>
      <div>
        <h5><span class="de">Kontakt</span><span class="en">Contact</span></h5>
        <ul>
          <li><a href="mailto:foto@blitzkneisser.com">foto@blitzkneisser.com</a></li>
          <li><a href="tel:+436643918228">+43 664 3918228</a></li>
          <li>Rohracker 6, 6092 Birgitz</li>
          <li><a href="https://www.instagram.com/blitzkneisser/" target="_blank" rel="noopener">Instagram @blitzkneisser</a></li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <span>© <span id="yr">2026</span> Andreas Kiss · Innsbruck, Tirol</span>
      <span><a href="/impressum/">Impressum</a> · <a href="/dsgvo/">Datenschutz</a> · <a href="/agb/">AGB</a></span>
    </div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>'''

def page(active, headhtml, body):
    return head(*headhtml) + header(active) + body + footer()

# =====================================================================
# INDEX
# =====================================================================
index_body = f'''
<main>
<section class="hero">
  <div class="wrap-wide hero-locator"><span>Innsbruck · Tirol</span></div>
  <div class="hero-media">
    <img src="{img('standesamt-hochzeit-innsbruck-nordkette-paar.jpg')}" alt="Brautpaar vor dem Nordkettenpanorama in Innsbruck" fetchpriority="high">
  </div>
  <div class="hero-inner">
    <div class="wrap-wide">
      <h1><span class="de">Echte Momente,<br>mitten in <em>Tirol</em>.</span><span class="en">Real moments,<br>in the heart of <em>Tyrol</em>.</span></h1>
      <p class="lead"><span class="de">Hochzeits-, Familien- und Porträtfotografie in Innsbruck und Umgebung – vom Standesamt bis zur kleinen Feier.</span><span class="en">Wedding, family and portrait photography in and around Innsbruck – from the registry office to the small celebration.</span></p>
      <div class="hero-cta">
        <a href="kontakt.html" class="btn btn-primary btn-lg"><span class="de">Termin anfragen</span><span class="en">Enquire now</span></a>
        <a href="portfolio.html" class="btn btn-light btn-lg"><span class="de">Portfolio ansehen</span><span class="en">See portfolio</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split narrow rev-mob">
      <div class="reveal">
        <div class="rule-sm"></div>
        <p class="kicker"><span class="de">Meine Haltung</span><span class="en">My approach</span></p>
        <h2 class="h-lg" style="margin-top:1.3rem;"><span class="de">Kein Showcharakter. Nur der echte Moment.</span><span class="en">No performance. Just the real moment.</span></h2>
        <div class="prose" style="margin-top:1.5rem;">
          <p class="muted"><span class="de">Die schönsten Bilder entstehen nicht, wenn alle posieren – sondern wenn ihr euch vergesst. Das Zittern beim Ja-Wort, das Lachen danach, die Hand, die die andere sucht. Ich bleibe leise im Hintergrund und halte fest, was zwischen euch wirklich passiert.</span><span class="en">The best pictures don't happen when everyone poses – they happen when you forget the camera. The trembling at the vows, the laughter after, the hand reaching for the other. I stay quietly in the background and capture what really happens between you.</span></p>
          <p class="muted"><span class="de">Kein Mindest-Gäste-Limit. Zu zweit, mit der Familie oder mit euren engsten Menschen – das Format bestimmt ihr.</span><span class="en">No minimum number of guests. Just the two of you, with family or your closest people – you decide the format.</span></p>
        </div>
        <a href="ueber-mich.html" class="link-u" style="margin-top:1.8rem;"><span class="de">Mehr über mich</span><span class="en">More about me</span> <span class="arw">→</span></a>
      </div>
      <figure class="reveal"><img class="ar-45" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-trausaal-kuss.jpg')}" alt="Erster Kuss im Trausaal des Standesamts Innsbruck"></figure>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="reveal" style="max-width:54ch;margin-bottom:clamp(2.5rem,5vw,3.5rem);">
      <p class="kicker"><span class="de">Leistungen</span><span class="en">Services</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Drei Wege, euren Moment festzuhalten.</span><span class="en">Three ways to capture your moment.</span></h2>
    </div>
    <div class="trio stagger reveal">
      <article class="feat">
        <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-altstadt-paar.jpg')}" alt="Standesamt Hochzeit Innsbruck – Paar in der Altstadt"></figure>
        <h3><span class="de">Standesamt &amp; kleine Hochzeiten</span><span class="en">Registry &amp; small weddings</span></h3>
        <p><span class="de">Eure Ziviltrauung in Innsbruck – kurz, dicht, echt. Danach Portraits in der Altstadt, am Inn oder in den Bergen.</span><span class="en">Your civil ceremony in Innsbruck – short, dense, real. Then portraits in the old town, by the river or in the mountains.</span></p>
        <a href="standesamt.html" class="link-u"><span class="de">Ansehen</span><span class="en">Explore</span> <span class="arw">→</span></a>
      </article>
      <article class="feat">
        <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-hofgasse-paar.jpg')}" alt="Familien- und Paarfotografie in der Innsbrucker Altstadt"></figure>
        <h3><span class="de">Familienfotografie</span><span class="en">Family photography</span></h3>
        <p><span class="de">Familienbilder, die nicht gestellt wirken, sondern nach euch aussehen – zuhause oder draußen in der Tiroler Landschaft.</span><span class="en">Family pictures that don't feel staged but look like you – at home or out in the Tyrolean landscape.</span></p>
        <a href="familie.html" class="link-u"><span class="de">Ansehen</span><span class="en">Explore</span> <span class="arw">→</span></a>
      </article>
      <article class="feat">
        <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-goldenes-dachl.jpg')}" alt="Paar- und Porträtfotografie beim Goldenen Dachl in Innsbruck"></figure>
        <h3><span class="de">Paar &amp; Porträt</span><span class="en">Couple &amp; portrait</span></h3>
        <p><span class="de">Verlobung, Jahrestag oder einfach so: entspannte Shootings, bei denen Bilder entstehen, die sich nach euch anfühlen.</span><span class="en">Engagement, anniversary or just because: relaxed sessions that make pictures which feel like you.</span></p>
        <a href="paar-portraet.html" class="link-u"><span class="de">Ansehen</span><span class="en">Explore</span> <span class="arw">→</span></a>
      </article>
    </div>
  </div>
</section>

<section class="band reveal">
  <img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-goldenes-dachl.jpg')}" alt="Innsbrucker Altstadt mit dem Goldenen Dachl">
  <div class="band-cap wrap-wide"><span class="de">Innsbruck – wo Stadt und Berge sich in wenigen Minuten berühren.</span><span class="en">Innsbruck – where city and mountains meet within minutes.</span></div>
</section>

<section class="section">
  <div class="wrap-wide">
    <div class="split" style="align-items:flex-end;margin-bottom:clamp(2rem,4vw,3rem);">
      <div class="reveal">
        <p class="kicker">Portfolio</p>
        <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Ausgewählte Arbeiten</span><span class="en">Selected work</span></h2>
      </div>
      <div class="reveal" style="align-self:flex-end;justify-self:end;"><a href="portfolio.html" class="link-u"><span class="de">Ganzes Portfolio</span><span class="en">Full portfolio</span> <span class="arw">→</span></a></div>
    </div>
    <div class="masonry reveal" data-lightbox>
      <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-altstadt-paar.jpg')}" alt="Standesamt Hochzeit Innsbruck Altstadt"><figcaption>Standesamt · Innsbruck</figcaption></figure>
      <figure><img loading="lazy" src="{img('Blitzkneisser-Hochzeit-Seefeld-8.jpg')}" alt="Hochzeit in Seefeld, Tirol"><figcaption>Hochzeit · Seefeld</figcaption></figure>
      <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-nordkette-paar.jpg')}" alt="Paar vor der Nordkette in Innsbruck"><figcaption>Nordkette · Innsbruck</figcaption></figure>
      <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-hofgasse-paar.jpg')}" alt="Paar in der Hofgasse, Innsbruck"><figcaption>Altstadt · Innsbruck</figcaption></figure>
      <figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-ringuebergabe.jpg')}" alt="Ringübergabe im Standesamt Innsbruck"><figcaption>Ja-Wort · Innsbruck</figcaption></figure>
      <figure><img loading="lazy" src="{img('Blitzkneisser-After-Wedding-Dolomites-3.jpg')}" alt="After-Wedding-Shooting in den Bergen"><figcaption><span class="de">Paar · Berge</span><span class="en">Couple · mountains</span></figcaption></figure>
    </div>
  </div>
</section>

<section class="section" style="background:var(--paper);">
  <div class="wrap">
    <div class="reveal center" style="margin-bottom:clamp(2.5rem,5vw,3.5rem);">
      <p class="kicker centered"><span class="de">Was Paare sagen</span><span class="en">What couples say</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Erinnerungen, die bleiben.</span><span class="en">Memories that stay.</span></h2>
    </div>
    <div class="reviews-grid stagger reveal">
      <figure class="review"><div class="stars">★★★★★</div><blockquote>“Andreas succeeded to catch emotions in photos in a way we have never seen in other wedding photos.”</blockquote><div class="who"><b>Kellie &amp; Krake</b> · <span class="de">Januar 2026</span><span class="en">January 2026</span></div></figure>
      <figure class="review"><div class="stars">★★★★★</div><blockquote>“Andi perfectly captures emotions in photos – they are just brilliant!”</blockquote><div class="who"><b>Anna &amp; Paul</b> · <span class="de">November 2025</span><span class="en">November 2025</span></div></figure>
      <figure class="review"><div class="stars">★★★★★</div><blockquote>“Photos that you'll enjoy looking at for a lifetime. Positive and helpful in all weathers – thank you.”</blockquote><div class="who"><b>Mary &amp; John</b> · <span class="de">August 2025</span><span class="en">August 2025</span></div></figure>
    </div>
  </div>
</section>
{cta()}
</main>'''

# =====================================================================
# STANDESAMT
# =====================================================================
standesamt_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide">
    <div class="phero-grid">
      <div class="reveal">
        <p class="kicker"><span class="de">Standesamt Innsbruck</span><span class="en">Registry office Innsbruck</span></p>
        <h1><span class="de">Standesamt &amp; <em>kleine Hochzeiten</em></span><span class="en">Registry office &amp; <em>small weddings</em></span></h1>
        <p class="lead"><span class="de">Eure Ziviltrauung in Innsbruck – ein kurzer, echter, tiefer Moment. Kein Stress, keine Inszenierung. Ich dokumentiere mit Ruhe und Gespür, was zwischen euch passiert: das Lachen vor dem Rathaus, das Zittern beim Ja-Wort, der erste Blick danach.</span><span class="en">Your civil ceremony in Innsbruck – a short, real, deep moment. No stress, no staging. I document with calm and instinct what happens between you: the laughter before the town hall, the trembling at the vows, the first glance after.</span></p>
        <a href="kontakt.html" class="btn btn-primary" style="margin-top:1.8rem;"><span class="de">Jetzt anfragen</span><span class="en">Enquire now</span></a>
      </div>
      <figure class="reveal"><img class="ar-45" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-altstadt-paar.jpg')}" alt="Standesamt Hochzeit Innsbruck – Paar in der Altstadt" fetchpriority="high"></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split narrow rev-mob">
      <div class="reveal">
        <div class="rule-sm"></div>
        <h2 class="h-md"><span class="de">Der ehrlichste Moment des ganzen Tages.</span><span class="en">The most honest moment of the whole day.</span></h2>
        <div class="prose muted" style="margin-top:1.4rem;">
          <p><span class="de">Das Standesamt hat keinen Showcharakter. Es ist kurz, dicht, echt. Zwei Menschen, ein Ja-Wort, ein Moment, der alles verändert. Genau das ist fotografisch eines der stärksten Ereignisse überhaupt – wenn man es wirklich sieht und nicht nur ablichtet.</span><span class="en">The registry office has no show to it. It's short, dense, real. Two people, one "yes", a moment that changes everything. That is one of the strongest things to photograph – when you truly see it rather than just record it.</span></p>
          <p><span class="de">Innsbruck bietet dafür eine außergewöhnliche Kulisse: historische Räume, die Altstadt danach, der Inn, die Berge – in wenigen Minuten Fahrt seid ihr mitten in der Natur.</span><span class="en">Innsbruck offers an extraordinary backdrop: historic rooms, the old town afterwards, the river Inn, the mountains – a few minutes' drive and you're out in nature.</span></p>
        </div>
      </div>
      <figure class="reveal"><img class="ar-34" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-trausaal-kuss.jpg')}" alt="Kuss im Trausaal, Standesamt Innsbruck"></figure>
    </div>
  </div>
</section>

<section class="section dark">
  <div class="wrap">
    <div class="split narrow">
      <div class="reveal">
        <p class="kicker on-dark"><span class="de">Innsbruck &amp; Umgebung</span><span class="en">Innsbruck &amp; around</span></p>
        <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Stadt und Berge in einem.</span><span class="en">City and mountains in one.</span></h2>
        <p style="margin-top:1.4rem;max-width:52ch;"><span class="de">Ihr seid in wenigen Minuten aus der Stadt heraus – und plötzlich stehen die Berge vor euch, so nah wie in kaum einer anderen Hauptstadt. Ich kenne die Orte und das Licht zu jeder Tageszeit und weiß, wann wir wo sein müssen. So könnt ihr einfach da sein, ohne Logistik-Stress.</span><span class="en">Within minutes you're out of the city – and suddenly the mountains stand before you, closer than in almost any other capital. I know the places and the light at every hour, and when we need to be where. So you can simply be present, without logistics stress.</span></p>
      </div>
      <ul class="placelist reveal">
        <li><i>01</i>Goldenes Dachl &amp; Altstadt</li>
        <li><i>02</i><span class="de">Rathaus · Maria-Theresien-Straße</span><span class="en">Town hall · Maria-Theresien-Str.</span></li>
        <li><i>03</i><span class="de">Inn mit Nordkettenblick</span><span class="en">River Inn &amp; Nordkette view</span></li>
        <li><i>04</i>Hofgarten</li>
        <li><i>05</i><span class="de">Nordkette &amp; Almen</span><span class="en">Nordkette &amp; alpine huts</span></li>
        <li><i>06</i><span class="de">Seefeld &amp; Umgebung</span><span class="en">Seefeld &amp; surroundings</span></li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(2.5rem,5vw,3.5rem);">
      <p class="kicker"><span class="de">Ablauf</span><span class="en">How it works</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Vom ersten Gedanken bis zu den Bildern.</span><span class="en">From the first thought to the photos.</span></h2>
    </div>
    <div class="steps reveal stagger">
      <div class="step"><span class="n">01</span><h4><span class="de">Anfrage</span><span class="en">Enquiry</span></h4><p><span class="de">Ihr schreibt mir kurz Datum, Ort und ein paar Worte zu euch.</span><span class="en">You send me the date, place and a few words about you.</span></p></div>
      <div class="step"><span class="n">02</span><h4><span class="de">Vorgespräch</span><span class="en">Pre-talk</span></h4><p><span class="de">Wir klären Ablauf, Timing und die schönsten Orte nach der Trauung.</span><span class="en">We plan the flow, timing and the best spots after the ceremony.</span></p></div>
      <div class="step"><span class="n">03</span><h4><span class="de">Trauung</span><span class="en">Ceremony</span></h4><p><span class="de">Im Saal bin ich leise und unsichtbar – kein Blitz, keine Posen.</span><span class="en">In the room I'm quiet and unseen – no flash, no poses.</span></p></div>
      <div class="step"><span class="n">04</span><h4><span class="de">Portraits</span><span class="en">Portraits</span></h4><p><span class="de">Danach führe ich euch zu Altstadt, Wasser oder Bergen – so weit ihr möchtet.</span><span class="en">Afterwards to the old town, water or mountains – as far as you like.</span></p></div>
    </div>
  </div>
</section>

<section class="section" style="background:var(--paper);">
  <div class="wrap">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(2rem,4vw,3rem);">
      <h2 class="h-md"><span class="de">Mehr als ein Fotograf am Standesamt.</span><span class="en">More than a photographer at the registry office.</span></h2>
    </div>
    <div class="trio stagger reveal">
      <div class="feat"><h3 class="h-md" style="font-size:1.3rem;"><span class="de">Auch für kleine Feiern</span><span class="en">For small celebrations</span></h3><p class="muted"><span class="de">Ob ihr danach im Stadel feiert, ins Restaurant geht oder in die Berge fahrt – ich begleite euch so weit, wie ihr möchtet.</span><span class="en">Whether you celebrate in a barn, go to a restaurant or head into the mountains – I accompany you as far as you like.</span></p></div>
      <div class="feat"><h3 class="h-md" style="font-size:1.3rem;"><span class="de">Internationale Paare</span><span class="en">International couples</span></h3><p class="muted"><span class="de">Viele internationale Paare wählen Innsbruck. Ich spreche Deutsch und Englisch und kenne die Abläufe gut.</span><span class="en">Many international couples choose Innsbruck. I speak German and English and know the procedures well.</span></p></div>
      <div class="feat"><h3 class="h-md" style="font-size:1.3rem;"><span class="de">Kein Gäste-Limit</span><span class="en">No guest minimum</span></h3><p class="muted"><span class="de">Trauung zu zweit? Gerne. Mit Familie? Auch. Das Format bestimmt ihr – ich passe mich an.</span><span class="en">Just the two of you? Gladly. With family? Also. You decide the format – I adapt.</span></p></div>
    </div>
  </div>
</section>

<section class="section faq">
  <div class="wrap">
    <div class="split narrow">
      <div class="reveal"><p class="kicker">FAQ</p><h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Häufige Fragen</span><span class="en">Common questions</span></h2></div>
      <div class="reveal">
        <details open><summary><span><span class="de">Wo ist das Standesamt in Innsbruck?</span><span class="en">Where is the registry office in Innsbruck?</span></span><span class="pl"></span></summary><p><span class="de">Im Rathaus in der Maria-Theresien-Straße 18, mitten in der Altstadt – umgeben von goldenen Dächern, historischen Fassaden und den nahen Gipfeln der Nordkette.</span><span class="en">In the town hall at Maria-Theresien-Straße 18, in the middle of the old town – surrounded by golden roofs, historic façades and the nearby peaks of the Nordkette.</span></p></details>
        <details><summary><span><span class="de">Fotografierst du auch ganz kleine Hochzeiten – nur zu zweit?</span><span class="en">Do you photograph very small weddings – just the two of us?</span></span><span class="pl"></span></summary><p><span class="de">Sehr gerne. Eine reine Standesamts-Trauung zu zweit oder mit wenigen Gästen ist oft das Intimste und Ehrlichste – und ich dokumentiere sie mit vollem Engagement.</span><span class="en">Very gladly. A registry-office ceremony just for two or with a few guests is often the most intimate and honest – and I document it with full dedication.</span></p></details>
        <details><summary><span><span class="de">Wie lange dauert eine Trauung?</span><span class="en">How long is the ceremony?</span></span><span class="pl"></span></summary><p><span class="de">Die eigentliche Zeremonie dauert meist 20 bis 40 Minuten. Ich empfehle, davor und danach Zeit für Portraits einzuplanen.</span><span class="en">The ceremony itself usually takes 20 to 40 minutes. I recommend leaving time before and after for portraits.</span></p></details>
        <details><summary><span><span class="de">Sprichst du Englisch für internationale Paare?</span><span class="en">Do you speak English for international couples?</span></span><span class="pl"></span></summary><p><span class="de">Ja. Ich spreche Deutsch und Englisch, kenne die Abläufe und helfe euch, bei den Dokumenten den Überblick zu behalten.</span><span class="en">Yes. I speak German and English, know the procedures and help you keep track of the paperwork.</span></p></details>
        <details><summary><span><span class="de">Können wir danach im Freien oder auf einer Alm feiern?</span><span class="en">Can we celebrate outdoors or at an alpine hut afterwards?</span></span><span class="pl"></span></summary><p><span class="de">Absolut. Viele Paare kombinieren die Innsbrucker Trauung mit einer Feier auf einer Alm oder in den Bergen. Ich begleite euch durch den ganzen Tag.</span><span class="en">Absolutely. Many couples combine the Innsbruck ceremony with a celebration at an alpine hut or in the mountains. I accompany you through the whole day.</span></p></details>
      </div>
    </div>
  </div>
</section>
{cta()}
</main>'''

# =====================================================================
# FAMILIE
# =====================================================================
familie_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide">
    <div class="phero-grid">
      <div class="reveal">
        <p class="kicker"><span class="de">Familienfotografie</span><span class="en">Family photography</span></p>
        <h1><span class="de">Familienbilder, die nach <em>euch</em> aussehen</span><span class="en">Family pictures that look like <em>you</em></span></h1>
        <p class="lead"><span class="de">Ihr wachst, verändert euch, gehört zusammen. Familienbilder, die nicht gestellt wirken – zuhause, im Garten oder draußen in der Tiroler Landschaft. Für kleine Familien, große Runden und die leisen Momente dazwischen.</span><span class="en">You grow, you change, you belong together. Family pictures that don't feel staged – at home, in the garden or out in the Tyrolean landscape. For small families, big gatherings and the quiet moments in between.</span></p>
        <a href="kontakt.html" class="btn btn-primary" style="margin-top:1.8rem;"><span class="de">Shooting anfragen</span><span class="en">Enquire</span></a>
      </div>
      <figure class="reveal"><img class="ar-45" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-hofgasse-paar.jpg')}" alt="Familien- und Paarfotografie in der Innsbrucker Altstadt" fetchpriority="high"></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split narrow rev-mob">
      <div class="reveal">
        <div class="rule-sm"></div>
        <h2 class="h-md"><span class="de">Kein Studio-Lächeln. Euer echtes Zusammensein.</span><span class="en">No studio smile. Your real togetherness.</span></h2>
        <div class="prose muted" style="margin-top:1.4rem;">
          <p><span class="de">Die schönsten Familienbilder entstehen in Bewegung: beim Spazieren, beim Toben der Kinder, beim ruhigen Moment am Ende. Ich gebe leichte Impulse, dränge aber nichts auf – so entstehen Bilder, die sich anfühlen wie ihr, nicht wie ein Fototermin.</span><span class="en">The best family pictures happen in motion: on a walk, while the kids run wild, in the quiet moment at the end. I give gentle prompts but never force a pose – so the pictures feel like you, not like an appointment.</span></p>
          <p><span class="de">Wir treffen uns dort, wo ihr euch wohlfühlt: bei euch zuhause, im eigenen Garten oder an einem Lieblingsort rund um Innsbruck.</span><span class="en">We meet where you feel at home: at your place, in your own garden or at a favourite spot around Innsbruck.</span></p>
        </div>
      </div>
      <figure class="reveal"><img class="ar-34" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-nordkette-paar.jpg')}" alt="Familie in der Tiroler Landschaft bei Innsbruck"></figure>
    </div>
  </div>
</section>

<section class="band reveal">
  <img loading="lazy" src="{img('Blitzkneisser-Hochzeit-Seefeld-8.jpg')}" alt="Familienmoment in der Tiroler Natur">
  <div class="band-cap wrap-wide"><span class="de">Draußen, wo Kinder Kinder sein dürfen.</span><span class="en">Outdoors, where children get to be children.</span></div>
</section>

<section class="section">
  <div class="wrap">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(2.5rem,5vw,3.5rem);">
      <p class="kicker"><span class="de">Anlässe</span><span class="en">Occasions</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Für jeden Abschnitt der richtige Moment.</span><span class="en">The right moment for every chapter.</span></h2>
    </div>
    <div class="trio stagger reveal">
      <div class="feat"><h3 class="h-md" style="font-size:1.3rem;"><span class="de">Zuhause &amp; draußen</span><span class="en">At home &amp; outdoors</span></h3><p class="muted"><span class="de">In euren eigenen vier Wänden oder an einem Lieblingsplatz in der Natur – dort, wo ihr euch am wohlsten fühlt.</span><span class="en">In your own home or at a favourite spot in nature – wherever you feel most at ease.</span></p></div>
      <div class="feat"><h3 class="h-md" style="font-size:1.3rem;"><span class="de">Neugeboren &amp; Kinder</span><span class="en">Newborn &amp; children</span></h3><p class="muted"><span class="de">Die ersten Wochen, der erste Geburtstag, der erste Schultag – Momente, die schneller vergehen, als man denkt.</span><span class="en">The first weeks, the first birthday, the first day of school – moments that pass faster than you think.</span></p></div>
      <div class="feat"><h3 class="h-md" style="font-size:1.3rem;"><span class="de">Jährliche Shootings</span><span class="en">Yearly sessions</span></h3><p class="muted"><span class="de">Einmal im Jahr festhalten, wie ihr euch verändert – eine kleine Tradition, die mit der Zeit unbezahlbar wird.</span><span class="en">Capture how you change once a year – a small tradition that becomes priceless over time.</span></p></div>
    </div>
  </div>
</section>

<section class="section faq" style="background:var(--paper);">
  <div class="wrap">
    <div class="split narrow">
      <div class="reveal"><p class="kicker">FAQ</p><h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Gut zu wissen</span><span class="en">Good to know</span></h2></div>
      <div class="reveal">
        <details open><summary><span><span class="de">Wo findet das Shooting statt?</span><span class="en">Where does the session take place?</span></span><span class="pl"></span></summary><p><span class="de">Wo ihr wollt: bei euch zuhause, im Garten oder an einem schönen Ort rund um Innsbruck. Wir besprechen vorab, was zu euch passt.</span><span class="en">Wherever you like: at home, in the garden or at a beautiful spot around Innsbruck. We discuss beforehand what suits you.</span></p></details>
        <details><summary><span><span class="de">Wie lange dauert ein Familienshooting?</span><span class="en">How long is a family session?</span></span><span class="pl"></span></summary><p><span class="de">Meist ein bis zwei Stunden – genug Zeit, damit alle ankommen und die Kinder auftauen können.</span><span class="en">Usually one to two hours – enough time for everyone to settle in and the kids to warm up.</span></p></details>
        <details><summary><span><span class="de">Was, wenn die Kinder nicht mitmachen?</span><span class="en">What if the kids won't cooperate?</span></span><span class="pl"></span></summary><p><span class="de">Genau dann entstehen die ehrlichsten Bilder. Ich arbeite ohne Zwang und mit viel Geduld – wir lassen den Kindern ihren Raum.</span><span class="en">That's exactly when the most honest pictures happen. I work without pressure and with a lot of patience – we give the kids their space.</span></p></details>
        <details><summary><span><span class="de">Bekommen wir die Bilder auch gedruckt?</span><span class="en">Can we get prints too?</span></span><span class="pl"></span></summary><p><span class="de">Gerne. Auf Wunsch bekommt ihr hochwertige Prints oder ein Fotoalbum – sprecht mich einfach darauf an.</span><span class="en">Gladly. On request you receive high-quality prints or a photo album – just ask me about it.</span></p></details>
      </div>
    </div>
  </div>
</section>
{cta()}
</main>'''

# =====================================================================
# PAAR & PORTRÄT
# =====================================================================
paar_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide">
    <div class="phero-grid">
      <div class="reveal">
        <p class="kicker"><span class="de">Paar &amp; Porträt</span><span class="en">Couple &amp; portrait</span></p>
        <h1><span class="de">Paar- &amp; Porträtshootings <em>ohne Pose</em></span><span class="en">Couple &amp; portrait sessions <em>without posing</em></span></h1>
        <p class="lead"><span class="de">Verlobung, Jahrestag oder einfach so. Entspannte Shootings in Innsbruck und Umgebung: Wir gehen ein Stück, reden, lachen – und nebenbei entstehen Bilder, die sich nach euch anfühlen, nicht nach einem Fotostudio.</span><span class="en">Engagement, anniversary or just because. Relaxed sessions in and around Innsbruck: we walk a little, talk, laugh – and along the way we make pictures that feel like you, not like a studio.</span></p>
        <a href="kontakt.html" class="btn btn-primary" style="margin-top:1.8rem;"><span class="de">Shooting anfragen</span><span class="en">Enquire</span></a>
      </div>
      <figure class="reveal"><img class="ar-45" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-goldenes-dachl.jpg')}" alt="Paar- und Porträtshooting beim Goldenen Dachl in Innsbruck" fetchpriority="high"></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split narrow rev-mob">
      <div class="reveal">
        <div class="rule-sm"></div>
        <h2 class="h-md"><span class="de">Ein Spaziergang, kein Fototermin.</span><span class="en">A walk, not a photo appointment.</span></h2>
        <div class="prose muted" style="margin-top:1.4rem;">
          <p><span class="de">Die meisten Paare sind am Anfang etwas nervös vor der Kamera – das ist völlig normal. Deshalb fangen wir langsam an: ein bisschen gehen, reden, ankommen. Nach zehn Minuten vergesst ihr, dass ich da bin, und genau dann entstehen die Bilder, die bleiben.</span><span class="en">Most couples are a little nervous in front of the camera at first – that's completely normal. So we start slowly: a bit of walking, talking, arriving. After ten minutes you forget I'm there, and that's exactly when the pictures that last appear.</span></p>
          <p><span class="de">Ideal als Verlobungsshooting, zum Jahrestag oder einfach, um festzuhalten, wo ihr gerade steht.</span><span class="en">Ideal as an engagement session, for an anniversary, or simply to capture where you are right now.</span></p>
        </div>
      </div>
      <figure class="reveal"><img class="ar-34" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-hofgasse-paar.jpg')}" alt="Entspanntes Paarshooting in der Innsbrucker Altstadt"></figure>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(2.5rem,5vw,3.5rem);">
      <p class="kicker"><span class="de">Anlässe</span><span class="en">Occasions</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Für den Moment, der zählt.</span><span class="en">For the moment that matters.</span></h2>
    </div>
    <div class="trio stagger reveal">
      <article class="feat"><figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-nordkette-paar.jpg')}" alt="Verlobungsshooting vor der Nordkette"></figure><h3><span class="de">Verlobung</span><span class="en">Engagement</span></h3><p class="muted"><span class="de">Frisch verlobt und mittendrin – wir halten das Gefühl fest, bevor die Planung beginnt.</span><span class="en">Freshly engaged and in the middle of it – we capture the feeling before the planning starts.</span></p></article>
      <article class="feat"><figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-altstadt-paar.jpg')}" alt="Paarshooting in Innsbruck"></figure><h3><span class="de">Paarshooting</span><span class="en">Couple session</span></h3><p class="muted"><span class="de">Zum Jahrestag oder einfach so: ein entspannter Nachmittag, der euch zeigt, wie ihr seid.</span><span class="en">For an anniversary or just because: a relaxed afternoon that shows you as you are.</span></p></article>
      <article class="feat"><figure><img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-goldenes-dachl.jpg')}" alt="Einzelporträt in Innsbruck"></figure><h3><span class="de">Einzelporträt</span><span class="en">Individual portrait</span></h3><p class="muted"><span class="de">Ein ehrliches Porträt für Beruf, Bewerbung oder euch selbst – natürlich, nicht steif.</span><span class="en">An honest portrait for work, applications or yourself – natural, not stiff.</span></p></article>
    </div>
  </div>
</section>

<section class="section" style="background:var(--paper);">
  <div class="wrap pull reveal">
    <blockquote><span class="de">„Ein starkes Bild sagt mehr als drei Adjektive."</span><span class="en">"One strong image says more than three adjectives."</span></blockquote>
    <cite>Andreas Kiss</cite>
  </div>
</section>
{cta()}
</main>'''

# =====================================================================
# PORTFOLIO
# =====================================================================
gallery_items = [
    ('standesamt-hochzeit-innsbruck-altstadt-paar.jpg','Standesamt Hochzeit Innsbruck Altstadt','Standesamt · Innsbruck'),
    ('Blitzkneisser-Hochzeit-Seefeld-8.jpg','Hochzeit in Seefeld, Tirol','Hochzeit · Seefeld'),
    ('standesamt-hochzeit-innsbruck-trausaal-kuss.jpg','Kuss im Trausaal, Standesamt Innsbruck','Trausaal · Innsbruck'),
    ('standesamt-hochzeit-innsbruck-nordkette-paar.jpg','Paar vor der Nordkette, Innsbruck','Nordkette · Innsbruck'),
    ('standesamt-hochzeit-innsbruck-hofgasse-paar.jpg','Paar in der Hofgasse, Innsbruck','Altstadt · Innsbruck'),
    ('standesamt-hochzeit-innsbruck-ringuebergabe.jpg','Ringübergabe im Standesamt Innsbruck','Ja-Wort · Innsbruck'),
    ('standesamt-hochzeit-innsbruck-goldenes-dachl.jpg','Paar beim Goldenen Dachl, Innsbruck','Goldenes Dachl · Innsbruck'),
    ('Blitzkneisser-After-Wedding-Dolomites-3.jpg','After-Wedding-Shooting in den Bergen','Paar · Berge'),
    ('Blitzkneisser-Mountain-Elopement-Instagram-5.jpg','Paarmoment in den Tiroler Bergen','Paar · Tirol'),
    ('Blitzkneisser-After-Wedding-Dolomites-11.jpg','After-Wedding in den Bergen','After Wedding · Berge'),
    ('Blitzkneisser-Mountain-Elopement-Instagram-27.jpg','Berghochzeit in Tirol','Berghochzeit · Tirol'),
    ('Blitzkneisser-Dolomites-Elopement-Wedding-155.jpg','Kleine Berghochzeit','Hochzeit · Berge'),
]
gfigs = "\n".join([f'      <figure><img loading="lazy" src="{img(n)}" alt="{a}"><figcaption>{c}</figcaption></figure>' for n,a,c in gallery_items])
portfolio_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide reveal">
    <p class="kicker">Portfolio</p>
    <h1><span class="de">Ausgewählte <em>Momente</em></span><span class="en">Selected <em>moments</em></span></h1>
    <p class="lead"><span class="de">Ein kuratierter Überblick aus Hochzeiten, kleinen Feiern, Standesamt-Trauungen und stillen Paarmomenten in Innsbruck und ganz Tirol.</span><span class="en">A curated look at weddings, small celebrations, registry-office ceremonies and quiet couple moments in Innsbruck and across Tyrol.</span></p>
  </div>
</section>
<section class="section">
  <div class="wrap-wide">
    <div class="masonry reveal" data-lightbox>
{gfigs}
    </div>
  </div>
</section>
{cta()}
</main>'''

# =====================================================================
# ÜBER MICH
# =====================================================================
ueber_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide">
    <div class="phero-grid">
      <div class="reveal">
        <p class="kicker"><span class="de">Über mich</span><span class="en">About</span></p>
        <h1><span class="de">Ich bin Andreas – <em>Fotograf aus Innsbruck</em></span><span class="en">I'm Andreas – <em>a photographer from Innsbruck</em></span></h1>
        <p class="lead"><span class="de">Ich lebe und arbeite in Tirol und kenne die Orte, an denen kleine Hochzeiten, Paarmomente und Familienbilder besonders stimmig wirken.</span><span class="en">I live and work in Tyrol and know the places where small weddings, couple moments and family pictures feel most at home.</span></p>
      </div>
      <figure class="reveal"><img class="ar-45" loading="lazy" src="{img('About-Me-Ich.webp')}" alt="Andreas Kiss, Hochzeitsfotograf aus Innsbruck" fetchpriority="high"></figure>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="prose reveal" style="max-width:64ch;">
      <p class="muted"><span class="de">Für mich geht es nicht darum, einzelne Momente abzuhaken, sondern euren Tag als stimmige Geschichte zu erzählen – mit Nähe, Ruhe, Licht und Persönlichkeit. Modern, emotional und ohne künstliche Inszenierung.</span><span class="en">For me it's not about ticking off single shots, but telling the story of your day – with closeness, calm, light and personality. Modern, emotional and without artificial staging.</span></p>
      <p class="muted"><span class="de">Ich bleibe lieber leise im Hintergrund, als euch in Posen zu drängen. Die stärksten Bilder entstehen, wenn ihr euch vergesst – und genau darauf warte ich. Ein starkes Bild sagt mir mehr als drei Adjektive.</span><span class="en">I'd rather stay quietly in the background than push you into poses. The strongest pictures happen when you forget the camera – and that's exactly what I wait for. One strong image tells me more than three adjectives.</span></p>
      <p class="muted"><span class="de">Ich spreche Deutsch und Englisch und begleite gern auch internationale Paare, die Innsbruck für ihre Trauung wählen.</span><span class="en">I speak German and English and am glad to accompany international couples who choose Innsbruck for their ceremony.</span></p>
    </div>
    <div class="reveal" style="margin-top:2.4rem;display:flex;flex-wrap:wrap;gap:2.5rem;padding-top:2rem;border-top:1px solid var(--line);">
      <div><div style="font-family:var(--serif);font-size:1.15rem;">Way Up North Awards 2024</div><div class="muted" style="font-size:.9rem;">Winner — Best Epic Portrait</div></div>
      <div><div style="font-family:var(--serif);font-size:1.15rem;">Rangefinder Magazine</div><div class="muted" style="font-size:.9rem;">Rf Photo of the Day — Lago di Braies</div></div>
    </div>
  </div>
</section>

<section class="band reveal">
  <img loading="lazy" src="{img('standesamt-hochzeit-innsbruck-nordkette-paar.jpg')}" alt="Innsbruck mit der Nordkette">
  <div class="band-cap wrap-wide"><span class="de">Zuhause in Innsbruck. Unterwegs in ganz Tirol.</span><span class="en">At home in Innsbruck. On the road across Tyrol.</span></div>
</section>
{cta()}
</main>'''

# =====================================================================
# KONTAKT
# =====================================================================
kontakt_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide reveal">
    <p class="kicker"><span class="de">Kontakt</span><span class="en">Contact</span></p>
    <h1><span class="de">Erzählt mir von euch und <em>eurem Tag</em></span><span class="en">Tell me about you and <em>your day</em></span></h1>
    <p class="lead"><span class="de">Nutzt das Formular für Hochzeiten, kleine Feiern, Familien- oder Porträtshootings. Ich antworte innerhalb von zwei Werktagen.</span><span class="en">Use the form for weddings, small celebrations, family or portrait sessions. I reply within two working days.</span></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split narrow">
      <div class="reveal">
        <div class="cinfo">
          <a href="mailto:foto@blitzkneisser.com"><span class="k">E-Mail</span>foto@blitzkneisser.com</a>
          <a href="tel:+436643918228"><span class="k"><span class="de">Telefon</span><span class="en">Phone</span></span>+43 664 3918228</a>
          <div><span class="k"><span class="de">Atelier</span><span class="en">Studio</span></span>Rohracker 6, 6092 Birgitz · Tirol</div>
          <a href="https://www.instagram.com/blitzkneisser/" target="_blank" rel="noopener"><span class="k">Instagram</span>@blitzkneisser</a>
        </div>
        <div style="margin-top:2.4rem;overflow:hidden;">
          <img class="ar-32" loading="lazy" src="{img('standesamt-hochzeit-innsbruck-altstadt-paar.jpg')}" alt="Paar in der Innsbrucker Altstadt" style="width:100%;object-fit:cover;">
        </div>
      </div>
      <form class="form reveal" id="contactForm" novalidate>
        <div class="two">
          <div class="field"><label for="name">Name</label><input id="name" name="name" type="text" required></div>
          <div class="field"><label for="email">E-Mail</label><input id="email" name="email" type="email" required></div>
        </div>
        <div class="two">
          <div class="field"><label for="date"><span class="de">Wunschdatum</span><span class="en">Preferred date</span></label><input id="date" name="date" type="text" placeholder="—"></div>
          <div class="field"><label for="place"><span class="de">Ort / Anlass</span><span class="en">Place / occasion</span></label><input id="place" name="place" type="text" placeholder="Innsbruck…"></div>
        </div>
        <div class="field"><label for="msg"><span class="de">Erzählt mir mehr</span><span class="en">Tell me more</span></label><textarea id="msg" name="msg" required></textarea></div>
        <button type="submit" class="btn btn-primary btn-lg" style="justify-self:start;"><span class="de">Anfrage senden</span><span class="en">Send enquiry</span></button>
        <p class="note"><span class="de">Mit dem Absenden öffnet sich euer E-Mail-Programm mit der fertigen Nachricht an mich.</span><span class="en">Submitting opens your email app with the message ready to send to me.</span></p>
      </form>
    </div>
  </div>
</section>
</main>'''

# =====================================================================
# PREISE / PAKETE
# =====================================================================
preise_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide reveal">
    <p class="kicker"><span class="de">Preise &amp; Pakete</span><span class="en">Pricing &amp; packages</span></p>
    <h1><span class="de">Klare Pakete, <em>fair kalkuliert</em></span><span class="en">Clear packages, <em>fairly priced</em></span></h1>
    <p class="lead"><span class="de">Transparente Richtwerte für Standesamt, kleine Hochzeiten, Familie und Porträt. Jedes Paket passe ich gern an euren Tag an – erzählt mir einfach, was ihr vorhabt.</span><span class="en">Transparent guide prices for registry office, small weddings, family and portrait. I'm happy to tailor each package to your day – just tell me what you have in mind.</span></p>
    <p class="pricenote" style="margin-top:1.6rem;"><b><span class="de">Inklusive:</span><span class="en">Included:</span></b> <span class="de">Vorgespräch · Anfahrt in Tirol · Online-Galerie · alle bearbeiteten Bilder digital &amp; ohne Wasserzeichen</span><span class="en">Pre-talk · travel within Tyrol · online gallery · all edited images digital &amp; watermark-free</span></p>
  </div>
</section>

<section class="section">
  <div class="wrap-wide">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(2rem,4vw,3rem);">
      <p class="kicker"><span class="de">Hochzeit</span><span class="en">Wedding</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Standesamt &amp; kleine Hochzeiten</span><span class="en">Registry office &amp; small weddings</span></h2>
    </div>
    <div class="pricing reveal">
      <div class="plan">
        <h3><span class="de">Standesamt kompakt</span><span class="en">Registry compact</span></h3>
        <div class="price">ab €490 <small><span class="de">/ ca. 1,5 Std.</span><span class="en">/ approx. 1.5 hrs</span></small></div>
        <p class="desc"><span class="de">Die Zeremonie und die schönsten Momente rundherum.</span><span class="en">The ceremony and the best moments around it.</span></p>
        <ul>
          <li><span class="de">Begleitung der Trauung</span><span class="en">Ceremony coverage</span></li>
          <li><span class="de">~30 Min Portraits danach</span><span class="en">~30 min portraits after</span></li>
          <li><span class="de">Alle Bilder digital</span><span class="en">All images digital</span></li>
          <li><span class="de">Private Online-Galerie</span><span class="en">Private online gallery</span></li>
        </ul>
        <a href="kontakt.html" class="link-u"><span class="de">Anfragen</span><span class="en">Enquire</span> <span class="arw">→</span></a>
      </div>
      <div class="plan featured">
        <span class="plan-tag"><span class="de">Beliebt</span><span class="en">Popular</span></span>
        <h3><span class="de">Standesamt &amp; Portraits</span><span class="en">Registry &amp; portraits</span></h3>
        <div class="price">ab €890 <small><span class="de">/ ca. 3–4 Std.</span><span class="en">/ approx. 3–4 hrs</span></small></div>
        <p class="desc"><span class="de">Trauung plus ausführliche Portraits in Stadt oder Natur.</span><span class="en">Ceremony plus a full portrait session in the city or nature.</span></p>
        <ul>
          <li><span class="de">Trauung &amp; Umgebung</span><span class="en">Ceremony &amp; surroundings</span></li>
          <li><span class="de">Portraits in Altstadt / an den Bergen</span><span class="en">Portraits in the old town / mountains</span></li>
          <li><span class="de">Location-Beratung vorab</span><span class="en">Location advice beforehand</span></li>
          <li><span class="de">Alle Bilder digital + Galerie</span><span class="en">All images digital + gallery</span></li>
        </ul>
        <a href="kontakt.html" class="btn btn-primary btn-sm"><span class="de">Anfragen</span><span class="en">Enquire</span></a>
      </div>
      <div class="plan">
        <h3><span class="de">Kleine Hochzeit</span><span class="en">Small wedding</span></h3>
        <div class="price">ab €1.490 <small><span class="de">/ bis ~8 Std.</span><span class="en">/ up to ~8 hrs</span></small></div>
        <p class="desc"><span class="de">Der ganze Tag – von den Vorbereitungen bis zur Feier.</span><span class="en">The whole day – from getting ready to the celebration.</span></p>
        <ul>
          <li><span class="de">Ganztägige Begleitung</span><span class="en">Full-day coverage</span></li>
          <li><span class="de">Mehrere Locations</span><span class="en">Several locations</span></li>
          <li><span class="de">Vorgespräch &amp; Timeline</span><span class="en">Pre-talk &amp; timeline</span></li>
          <li><span class="de">Alle Bilder digital + Galerie</span><span class="en">All images digital + gallery</span></li>
        </ul>
        <a href="kontakt.html" class="link-u"><span class="de">Anfragen</span><span class="en">Enquire</span> <span class="arw">→</span></a>
      </div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="wrap-wide">
    <div class="reveal" style="max-width:52ch;margin-bottom:clamp(2rem,4vw,3rem);">
      <p class="kicker"><span class="de">Shootings</span><span class="en">Sessions</span></p>
      <h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Familie, Paar &amp; Porträt</span><span class="en">Family, couple &amp; portrait</span></h2>
    </div>
    <div class="pricing reveal">
      <div class="plan">
        <h3><span class="de">Porträt</span><span class="en">Portrait</span></h3>
        <div class="price">ab €190 <small><span class="de">/ ca. 1 Std.</span><span class="en">/ approx. 1 hr</span></small></div>
        <p class="desc"><span class="de">Ein ehrliches Einzelporträt – für Beruf oder euch selbst.</span><span class="en">An honest individual portrait – for work or yourself.</span></p>
        <ul>
          <li><span class="de">1 Location in Innsbruck</span><span class="en">1 location in Innsbruck</span></li>
          <li><span class="de">Die schönsten Bilder digital</span><span class="en">Best images digital</span></li>
          <li><span class="de">Private Online-Galerie</span><span class="en">Private online gallery</span></li>
        </ul>
        <a href="kontakt.html" class="link-u"><span class="de">Anfragen</span><span class="en">Enquire</span> <span class="arw">→</span></a>
      </div>
      <div class="plan featured">
        <span class="plan-tag"><span class="de">Beliebt</span><span class="en">Popular</span></span>
        <h3><span class="de">Familienshooting</span><span class="en">Family session</span></h3>
        <div class="price">ab €290 <small><span class="de">/ ca. 1–1,5 Std.</span><span class="en">/ approx. 1–1.5 hrs</span></small></div>
        <p class="desc"><span class="de">Zuhause oder draußen – euer echtes Zusammensein.</span><span class="en">At home or outdoors – your real togetherness.</span></p>
        <ul>
          <li><span class="de">Ort eurer Wahl in &amp; um Innsbruck</span><span class="en">Location of your choice around Innsbruck</span></li>
          <li><span class="de">Entspannt, ohne Zwang</span><span class="en">Relaxed, no pressure</span></li>
          <li><span class="de">Alle Bilder digital + Galerie</span><span class="en">All images digital + gallery</span></li>
        </ul>
        <a href="kontakt.html" class="btn btn-primary btn-sm"><span class="de">Anfragen</span><span class="en">Enquire</span></a>
      </div>
      <div class="plan">
        <h3><span class="de">Paar &amp; Verlobung</span><span class="en">Couple &amp; engagement</span></h3>
        <div class="price">ab €290 <small><span class="de">/ ca. 1–1,5 Std.</span><span class="en">/ approx. 1–1.5 hrs</span></small></div>
        <p class="desc"><span class="de">Ein Spaziergang zu zweit, bei dem echte Bilder entstehen.</span><span class="en">A walk for two that turns into real pictures.</span></p>
        <ul>
          <li><span class="de">Location nach Absprache</span><span class="en">Location by arrangement</span></li>
          <li><span class="de">Ideal zur Verlobung / zum Jahrestag</span><span class="en">Ideal for engagement / anniversary</span></li>
          <li><span class="de">Alle Bilder digital + Galerie</span><span class="en">All images digital + gallery</span></li>
        </ul>
        <a href="kontakt.html" class="link-u"><span class="de">Anfragen</span><span class="en">Enquire</span> <span class="arw">→</span></a>
      </div>
    </div>
    <p class="muted reveal" style="margin-top:1.8rem;font-size:.86rem;max-width:70ch;"><span class="de">Alle Preise sind Richtwerte inkl. USt. und dienen der Orientierung. Prints, Alben, zusätzliche Stunden oder weitere Anfahrt gern auf Anfrage. Für ein individuelles Angebot schreibt mir einfach.</span><span class="en">All prices are guide values incl. VAT and for orientation. Prints, albums, extra hours or longer travel are available on request. For an individual quote, just get in touch.</span></p>
  </div>
</section>

<section class="section faq" style="background:var(--paper);">
  <div class="wrap">
    <div class="split narrow">
      <div class="reveal"><p class="kicker">FAQ</p><h2 class="h-lg" style="margin-top:1.2rem;"><span class="de">Zu den Preisen</span><span class="en">About pricing</span></h2></div>
      <div class="reveal">
        <details open><summary><span><span class="de">Sind die Preise fix?</span><span class="en">Are the prices fixed?</span></span><span class="pl"></span></summary><p><span class="de">Es sind Richtwerte. Jede Hochzeit und jedes Shooting ist anders – nach einem kurzen Gespräch bekommt ihr ein passendes, transparentes Angebot ohne versteckte Kosten.</span><span class="en">They are guide values. Every wedding and session is different – after a short talk you'll get a fitting, transparent quote with no hidden costs.</span></p></details>
        <details><summary><span><span class="de">Wie viele Bilder bekommen wir?</span><span class="en">How many images do we get?</span></span><span class="pl"></span></summary><p><span class="de">Ihr bekommt alle gelungenen, bearbeiteten Bilder – nicht künstlich limitiert. Wie viele es werden, hängt von der Dauer ab, meist mehrere Dutzend bis mehrere Hundert.</span><span class="en">You receive all the good, edited images – not artificially limited. How many depends on the duration, usually several dozen to several hundred.</span></p></details>
        <details><summary><span><span class="de">Ist die Anfahrt inklusive?</span><span class="en">Is travel included?</span></span><span class="pl"></span></summary><p><span class="de">Innerhalb Tirols ist die Anfahrt inklusive. Für weitere Strecken oder Hochzeiten außerhalb Tirols mache ich euch gern ein individuelles Angebot.</span><span class="en">Within Tyrol, travel is included. For longer distances or weddings outside Tyrol I'm happy to make an individual offer.</span></p></details>
        <details><summary><span><span class="de">Gibt es Prints oder Alben?</span><span class="en">Are prints or albums available?</span></span><span class="pl"></span></summary><p><span class="de">Ja. Auf Wunsch bekommt ihr hochwertige Prints oder ein handgefertigtes Fotoalbum – sprecht mich einfach darauf an.</span><span class="en">Yes. On request you receive high-quality prints or a handmade photo album – just ask me.</span></p></details>
      </div>
    </div>
  </div>
</section>
{cta()}
</main>'''

# =====================================================================
# GUIDE (Ratgeber, Tirol) — Uebersicht + einzelne Beitraege
# =====================================================================
GUIDES = [
  {
    "slug": "guide-standesamt-innsbruck.html",
    "hero": "standesamt-hochzeit-innsbruck-goldenes-dachl.jpg",
    "cat_de": "Ratgeber · Innsbruck", "cat_en": "Guide · Innsbruck",
    "read_de": "6 Min", "read_en": "6 min", "date_iso": "2026-07-22", "date_de": "Juli 2026", "date_en": "July 2026",
    "title_de": "Standesamt Innsbruck: Ablauf, Termine &amp; die schönsten Foto-Spots",
    "title_en": "Getting married at Innsbruck registry office: process, dates &amp; the best photo spots",
    "excerpt_de": "Alles, was ihr für eure Ziviltrauung in Innsbruck wissen müsst – vom Termin über den Ablauf bis zu den schönsten Orten für Bilder danach.",
    "excerpt_en": "Everything you need for your civil ceremony in Innsbruck – from booking to the process to the best places for photos afterwards.",
    "body_de": '''
<p>Das Standesamt hat keinen Showcharakter. Es ist kurz, dicht, echt – zwei Menschen, ein Ja-Wort, ein Moment, der alles verändert. Innsbruck ist dafür einer der schönsten Orte in Tirol: historische Räume, die Altstadt gleich nebenan und in wenigen Minuten die Berge. Hier findet ihr alles Wichtige für eure Ziviltrauung an einem Ort.</p>
<h2>Wo ist das Standesamt in Innsbruck?</h2>
<p>Das Standesamt der Stadt Innsbruck befindet sich im Rathaus in der Maria-Theresien-Straße 18, mitten in der Altstadt. Ihr seid damit direkt zwischen Goldenem Dachl, historischen Fassaden und dem Blick auf die Nordkette – ideale Voraussetzungen für Portraits gleich nach der Trauung.</p>
<h2>Wie ihr euren Termin bekommt</h2>
<p>Standesamtliche Trauungen werden direkt über die Stadt Innsbruck gebucht. Meldet euch früh, gerade für beliebte Sommer- und Herbsttermine. Für die Anmeldung braucht ihr in der Regel gültige Lichtbildausweise, Geburtsurkunden und – je nach Situation – weitere Dokumente.</p>
<div class="callout"><b>Für internationale Paare:</b> Innsbruck ist bei Paaren aus dem Ausland beliebt. Hier gibt es ein paar Besonderheiten bei den Dokumenten (beglaubigte Übersetzungen, Ehefähigkeitszeugnis o. Ä.). Plant dafür etwas Vorlauf ein – ich unterstütze euch gern dabei, den Überblick zu behalten.</div>
<h2>Wie der Tag abläuft</h2>
<p>Die eigentliche Zeremonie dauert meist 20 bis 40 Minuten. Ich empfehle, davor und danach Zeit einzuplanen: ein paar Minuten zum Ankommen, die Trauung selbst, dann Zeit für Portraits. Im Trausaal bin ich leise und unsichtbar – kein Blitz, keine gestellten Posen, nur das, was wirklich passiert.</p>
<h2>Die schönsten Foto-Spots nach der Trauung</h2>
<p>Das Besondere an Innsbruck: Ihr habt Stadt und Berge in wenigen Minuten. Diese Orte funktionieren fast immer:</p>
<ul>
<li>Goldenes Dachl &amp; die Gassen der Altstadt – klassisch, historisch, typisch Innsbruck</li>
<li>Der Inn mit Nordkettenblick – Wasser, Farben und Berge in einem Bild</li>
<li>Der Hofgarten – ruhig, grün, ideal bei Sonne</li>
<li>Maria-Theresien-Straße mit Blick auf die Nordkette</li>
<li>Eine kurze Fahrt hinauf – Nordkette oder eine Alm für Bergkulisse</li>
<li>Seefeld und Umgebung, wenn ihr etwas weiter hinaus möchtet</li>
</ul>
<h2>Das beste Licht &amp; die beste Uhrzeit</h2>
<p>In der Altstadt ist das Licht am Vormittag und späten Nachmittag am schönsten – mittags wird es hart. Für weiche, warme Bilder ist die goldene Stunde kurz vor Sonnenuntergang ideal. Ich kenne die Orte und das Licht zu jeder Tageszeit und plane den Ablauf so, dass wir zur richtigen Zeit am richtigen Ort sind.</p>
<h2>Klein feiern nach dem Standesamt</h2>
<p>Viele Paare kombinieren die Innsbrucker Trauung mit einer kleinen Feier – im Stadel, auf einer Alm, im Lieblingsrestaurant oder einfach zu zweit in den Bergen. Es gibt kein Mindest-Gäste-Limit: Das Format bestimmt ihr, ich begleite euch so weit, wie ihr möchtet.</p>
''',
    "body_en": '''
<p>The registry office has no show to it. It's short, dense, real – two people, one "yes", a moment that changes everything. Innsbruck is one of the loveliest places in Tyrol for it: historic rooms, the old town next door, and the mountains just minutes away. Here's everything that matters for your civil ceremony, in one place.</p>
<h2>Where is the registry office in Innsbruck?</h2>
<p>Innsbruck's registry office is in the town hall at Maria-Theresien-Straße 18, right in the old town – between the Golden Roof, historic façades and the view of the Nordkette. Perfect conditions for portraits straight after the ceremony.</p>
<h2>How to get your date</h2>
<p>Civil ceremonies are booked directly through the City of Innsbruck. Get in touch early, especially for popular summer and autumn dates. For registration you usually need valid photo IDs, birth certificates and – depending on your situation – further documents.</p>
<div class="callout"><b>For international couples:</b> Innsbruck is popular with couples from abroad. There are a few specifics around documents (certified translations, certificate of no impediment, etc.). Allow some lead time – I'm glad to help you keep track.</div>
<h2>How the day unfolds</h2>
<p>The ceremony itself usually takes 20 to 40 minutes. I recommend leaving time before and after: a few minutes to arrive, the ceremony, then time for portraits. In the room I stay quiet and unseen – no flash, no staged poses, just what really happens.</p>
<h2>The best photo spots after the ceremony</h2>
<p>What makes Innsbruck special: you have city and mountains within minutes. These places almost always work:</p>
<ul>
<li>The Golden Roof &amp; the old-town lanes – classic, historic, unmistakably Innsbruck</li>
<li>The river Inn with the Nordkette behind – water, colour and mountains in one frame</li>
<li>The Hofgarten – calm, green, ideal in sunshine</li>
<li>Maria-Theresien-Straße with the Nordkette view</li>
<li>A short drive up – the Nordkette or an alpine hut for a mountain backdrop</li>
<li>Seefeld and around, if you'd like to go a little further</li>
</ul>
<h2>The best light &amp; time of day</h2>
<p>In the old town the light is loveliest in the morning and late afternoon – midday gets harsh. For soft, warm images the golden hour just before sunset is ideal. I know the places and the light at every hour and plan the day so we're in the right spot at the right time.</p>
<h2>A small celebration afterwards</h2>
<p>Many couples pair the Innsbruck ceremony with a small celebration – in a barn, at an alpine hut, in a favourite restaurant, or simply the two of you in the mountains. There's no minimum number of guests: you decide the format, I accompany you as far as you like.</p>
''',
  },
]

def guide_ldjson(g):
    return ('<script type="application/ld+json">{"@context":"https://schema.org","@type":"Article",'
            '"headline":"%s","datePublished":"%s","inLanguage":"de",'
            '"author":{"@type":"Person","name":"Andreas Kiss"},'
            '"publisher":{"@type":"Organization","name":"Andreas Kiss – Hochzeitsfotograf Tirol"},'
            '"about":"Standesamt Innsbruck, Hochzeitsfotografie Tirol"}</script>'
            ) % (g["title_de"].replace('&amp;','&'), g["date_iso"])

def guide_page_body(g):
    return f'''
<main>
<article class="section article">
  <a href="guide.html" class="link-u article-back"><span class="arw">←</span> <span class="de">Alle Guides</span><span class="en">All guides</span></a>
  <div class="reveal">
    <p class="kicker"><span class="de">{g["cat_de"]}</span><span class="en">{g["cat_en"]}</span></p>
    <h1 class="h-xl" style="margin-top:1.1rem;font-size:clamp(2rem,1.4rem + 3vw,3.4rem);"><span class="de">{g["title_de"]}</span><span class="en">{g["title_en"]}</span></h1>
    <div class="a-meta"><span class="de">{g["date_de"]} · {g["read_de"]} Lesezeit</span><span class="en">{g["date_en"]} · {g["read_en"]} read</span></div>
  </div>
  <figure class="article-hero reveal"><img loading="lazy" src="{img(g["hero"])}" alt="{g["cat_de"]}"></figure>
  <div class="article-body reveal">
    <div class="de">{g["body_de"]}</div>
    <div class="en">{g["body_en"]}</div>
  </div>
  <div class="article-body reveal" style="margin-top:2.5rem;padding-top:2rem;border-top:1px solid var(--line);">
    <p style="font-family:var(--display);font-size:1.15rem;color:var(--ink);"><span class="de">Plant ihr eure Trauung in Innsbruck? Erzählt mir davon – ich begleite euch mit Ruhe und Gespür.</span><span class="en">Planning your ceremony in Innsbruck? Tell me about it – I'll be there, calm and attentive.</span></p>
    <a href="kontakt.html" class="btn btn-primary" style="margin-top:1.2rem;"><span class="de">Termin anfragen</span><span class="en">Enquire now</span></a>
  </div>
  {guide_ldjson(g)}
</article>
</main>'''

def guide_cards():
    out = []
    for g in GUIDES:
        out.append(f'''
      <article class="gcard reveal">
        <a href="{g["slug"]}"><figure><img loading="lazy" src="{img(g["hero"])}" alt="{g["cat_de"]}"></figure></a>
        <span class="cat"><span class="de">{g["cat_de"]}</span><span class="en">{g["cat_en"]}</span></span>
        <h3><a href="{g["slug"]}"><span class="de">{g["title_de"]}</span><span class="en">{g["title_en"]}</span></a></h3>
        <p><span class="de">{g["excerpt_de"]}</span><span class="en">{g["excerpt_en"]}</span></p>
        <a href="{g["slug"]}" class="link-u"><span class="de">Weiterlesen</span><span class="en">Read more</span> <span class="arw">→</span></a>
      </article>''')
    return "\n".join(out)

guide_index_body = f'''
<main>
<section class="phero">
  <div class="wrap-wide reveal">
    <p class="kicker">Guide · Tirol</p>
    <h1><span class="de">Der Tirol-<em>Hochzeitsguide</em></span><span class="en">The Tyrol <em>wedding guide</em></span></h1>
    <p class="lead"><span class="de">Ehrliche Tipps aus der Praxis rund ums Heiraten in Innsbruck und Tirol – Standesamt, Locations, Timing und Licht. Damit ihr entspannt planen könnt.</span><span class="en">Honest, practical tips on getting married in Innsbruck and Tyrol – registry office, locations, timing and light. So you can plan with ease.</span></p>
  </div>
</section>
<section class="section">
  <div class="wrap-wide">
    <div class="guide-grid">
{guide_cards()}
    </div>
    <p class="muted reveal" style="margin-top:2.5rem;font-size:.9rem;"><span class="de">Weitere Guides folgen – u. a. „Heiraten in Tirol: die schönsten Locations", „Berghochzeit planen" und „Beste Jahres- &amp; Tageszeit für Bergfotos".</span><span class="en">More guides coming soon – incl. "Getting married in Tyrol: the best locations", "Planning a mountain wedding" and "Best season &amp; time of day for mountain photos".</span></p>
  </div>
</section>
{cta()}
</main>'''

# ---------- WRITE ----------
pages = {
  'index.html': ('', ('Andreas Kiss – Hochzeitsfotograf Innsbruck & Tirol','Hochzeits-, Familien- und Porträtfotografie in Innsbruck und Tirol. Vom Standesamt bis zur kleinen Feier – ruhig, ehrlich, ohne Inszenierung.'), index_body),
  'standesamt.html': ('standesamt.html', ('Standesamt Hochzeit Innsbruck & kleine Hochzeiten | Andreas Kiss','Fotograf für eure Standesamt-Hochzeit in Innsbruck und kleine Feiern in Tirol. Ruhig, dokumentarisch, ohne Inszenierung.'), standesamt_body),
  'familie.html': ('familie.html', ('Familienfotografie Innsbruck & Tirol | Andreas Kiss','Natürliche Familienfotografie in Innsbruck und Tirol – zuhause, im Garten oder draußen in der Natur.'), familie_body),
  'paar-portraet.html': ('paar-portraet.html', ('Paar- & Porträtfotografie Innsbruck | Andreas Kiss','Entspannte Paar-, Verlobungs- und Porträtshootings in Innsbruck und Tirol – ohne steife Posen.'), paar_body),
  'portfolio.html': ('portfolio.html', ('Portfolio | Andreas Kiss – Hochzeitsfotograf Tirol','Ausgewählte Hochzeits-, Standesamt- und Paarfotografie aus Innsbruck und Tirol.'), portfolio_body),
  'preise.html': ('preise.html', ('Preise & Pakete | Andreas Kiss – Fotograf Innsbruck & Tirol','Transparente Preise für Standesamt, kleine Hochzeiten, Familien- und Paarfotografie in Innsbruck und Tirol.'), preise_body),
  'guide.html': ('guide.html', ('Hochzeitsguide Tirol – Standesamt, Locations & Tipps | Andreas Kiss','Praktische Tipps zum Heiraten in Innsbruck und Tirol: Standesamt, Foto-Locations, Timing und Licht – ehrlich und aus der Praxis.'), guide_index_body),
  'ueber-mich.html': ('ueber-mich.html', ('Über mich – Andreas Kiss, Fotograf aus Innsbruck','Andreas Kiss, Hochzeits- und Porträtfotograf aus Innsbruck. Ruhig, ehrlich, dokumentarisch.'), ueber_body),
  'kontakt.html': ('kontakt.html', ('Kontakt | Andreas Kiss – Hochzeitsfotograf Innsbruck','Anfrage für Hochzeit, Standesamt, Familie oder Porträt in Innsbruck und Tirol.'), kontakt_body),
}
# register single guide article pages
for g in GUIDES:
    pages[g["slug"]] = ('guide.html',
        (g["title_de"].replace('&amp;','&') + ' | Andreas Kiss', g["excerpt_de"]),
        guide_page_body(g))

for fn,(active,hd,body) in pages.items():
    with open(os.path.join(OUT, fn),'w',encoding='utf-8') as f:
        f.write(page(active, hd, body))
    print("wrote", fn)

# ---------- local images: folder + download script ----------
imgdir = os.path.join(OUT, "assets", "img")
os.makedirs(imgdir, exist_ok=True)
open(os.path.join(imgdir, ".gitkeep"), "w").close()

sh = ["#!/usr/bin/env bash",
      "# Laedt alle verwendeten Bilder von der Live-Seite nach assets/img/.",
      "# Einmal ausfuehren:  bash download-images.sh",
      "set -e",
      'cd "$(dirname "$0")/assets/img"',
      'BASE="https://hochzeitsfotograf.tirol/assets/uploads"',
      'echo "Lade %d Bilder ..."' % len(USED)]
for n in sorted(USED):
    sh.append('curl -fSL "$BASE/%s" -o "%s" && echo "  ok %s"' % (n, n, n))
sh.append('echo "Fertig – alle Bilder liegen jetzt in assets/img/."')
with open(os.path.join(OUT, "download-images.sh"), "w", encoding="utf-8") as f:
    f.write("\n".join(sh) + "\n")
os.chmod(os.path.join(OUT, "download-images.sh"), 0o755)
print("wrote download-images.sh for", len(USED), "images")
