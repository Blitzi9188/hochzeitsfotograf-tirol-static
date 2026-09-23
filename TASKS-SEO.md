# Claude-Code-Prompt: SEO- & Conversion-Ausbau der Website

> Kopiere alles unter der Linie in Claude Code (im entpackten Projektordner ausführen). Passe Kursives bei Bedarf an.

---

Du arbeitest an einer bestehenden, statischen, mehrsprachigen Foto­grafen-Website. **Lies zuerst `build.py`, `assets/site.css` und `assets/site.js`, um die Architektur zu verstehen, bevor du etwas änderst.**

## Projekt-Architektur (wichtig)
- Die HTML-Seiten werden **NICHT von Hand** gepflegt, sondern von **`build.py`** (Python) erzeugt. `python3 build.py` schreibt `index.html`, `standesamt.html`, `familie.html`, `paar-portraet.html`, `preise.html`, `portfolio.html`, `ueber-mich.html`, `kontakt.html`. **Alle Änderungen an Seiteninhalt/Struktur MÜSSEN in `build.py` erfolgen**, danach neu bauen. Ändere generierte `.html` nie direkt.
- Gemeinsam: `assets/site.css` (Design-System, OKLCH-Tokens) und `assets/site.js` (Sprache, Nav, Reveal, Lightbox, Bild-Fallback, mailto-Formular).
- **Zweisprachigkeit DE/EN:** jeder übersetzte Text steht als `<span class="de">…</span><span class="en">…</span>` im DOM; CSS blendet je nach `html[data-lang]` aus. Diesen Pattern bei ALLEM Neuen beibehalten.
- Bilder: `assets/img/DATEINAME`; `site.js` lädt bei Fehler automatisch von `https://hochzeitsfotograf.tirol/assets/uploads/` nach. Deutscher Alt-Text.
- Design bleibt: ruhig/editorial, Fraunces + Inter, tiefes Tannengrün als einziger Akzent. Keine neuen Frameworks. Reveal-Failsafe, `prefers-reduced-motion`, Barrierefreiheit und flache Navigation beibehalten.

## Marke / Fakten (real verwenden)
Andreas Kiss — Hochzeits-, Familien- & Porträtfotograf, **lokal Innsbruck/Tirol** (Standesamt & kleine Hochzeiten, Familie, Paar/Porträt). E-Mail foto@blitzkneisser.com · Tel/WhatsApp +43 664 3918228 · Rohracker 6, 6092 Birgitz, Tirol · Instagram @blitzkneisser · Domain hochzeitsfotograf.tirol. Auszeichnungen: Way Up North Awards 2024 „Best Epic Portrait", Rangefinder Magazine.

## Ziel
Setze die folgenden SEO- und Conversion-Verbesserungen um (Ergebnis einer Wettbewerbsanalyse Tiroler Fotografen). Reihenfolge = Priorität.

### 1. Strukturierte Daten (JSON-LD)
- In `head()` von `build.py` ein `LocalBusiness`/`ProfessionalService`-Schema einbauen (name, image, url, telephone, email, address mit PostalAddress Birgitz/Tirol, geo, `areaServed` Innsbruck + Tirol, `priceRange` „€€", sameAs Instagram). Auf allen Seiten.
- Auf Seiten mit FAQ (standesamt, familie, preise, ggf. kontakt) zusätzlich **`FAQPage`**-Schema, generiert aus denselben Fragen/Antworten (deutsche Fassung).
- **`AggregateRating` + `Review`** aus den 3 vorhandenen Google-Bewertungen (Kellie & Krake, Anna & Paul, Mary & John), ratingValue 5.
- JSON-LD valide halten (kein Komma-Fehler); pro Seite nur passende Typen.

### 2. Meta / Social / Technik
- Pro Seite eindeutige `<title>` und `meta description` (größtenteils vorhanden — prüfen/schärfen mit Keyword + Ort).
- **Open Graph + Twitter Card** ergänzen (og:title, og:description, og:image = ein starkes Bild, og:url, og:type, og:locale de_AT + alternate en). `<link rel="canonical">` pro Seite. Favicon einbinden (Platzhalter `assets/favicon.svg` anlegen).
- **`sitemap.xml` und `robots.txt`** über `build.py` mit erzeugen (alle Seiten, Domain hochzeitsfotograf.tirol).
- Bild-Performance: allen `<img>` sinnvolle `width`/`height` bzw. `aspect-ratio` geben (gegen Layout-Shift), Hero-Bild mit `<link rel="preload" as="image">`. Kommentar/Hinweis ergänzen, Bilder als WebP zu exportieren.

### 3. Conversion-Elemente
- **Verfügbarkeits-CTA** als wiederverwendbaren Block: „Ist euer Datum noch frei?" / „Is your date still available?" → Link auf kontakt.html. Auf Startseite und Leistungsseiten platzieren (dezent, im Design-System).
- **WhatsApp-Button** (floating, unten rechts) → `https://wa.me/436643918228`, mit `aria-label`, DE/EN Tooltip, respektiert reduced-motion. Nicht aufdringlich.
- Kurzen **Ablauf/Prozess** (Anfrage → Vorgespräch → Termin → Bildergalerie) auch auf Startseite oder Kontakt zeigen (Komponente `.steps` existiert bereits).

### 4. Regionale SEO-Tiefe
- **„Regionen in Tirol"-Sektion** (oder Footer-Block) mit Orten: Innsbruck, Hall, Seefeld, Achensee, Stubaital, Wipptal, Zillertal, Ötztal, Kitzbühel, Telfs. Orte auch natürlich in Fließtexte einstreuen (nicht spammy).

### 5. Journal/Blog (Grundgerüst)
- Neue Seite **`journal.html`** (Übersicht) + Nav-/Footer-Eintrag „Journal". Karten-/Listenlayout für Beiträge.
- **Beitrags-Template** + 1 Beispielbeitrag (`journal-standesamt-innsbruck.html`) mit dem Aufbau: GROSSBUCHSTABEN-Titel, kurzer Hook mit Gegensatz, Bildergalerie, Abschluss-CTA. Pro Beitrag `Article`/`BlogPosting`-JSON-LD, `meta description`, deutscher Alt-Text. Struktur so bauen, dass sich weitere Beiträge leicht ergänzen lassen (Liste/Datenstruktur in `build.py`).

### 6. Optional (wenn Zeit)
- Eigene Seite **`after-wedding.html`** (nachgefragtes Tirol-Keyword), analog zu den anderen Leistungsseiten, in Nav/Footer.
- Testimonials ausbauen (längere, namentliche Zitate).

## Randbedingungen & Abnahme
- Nur `build.py` + `assets/*` ändern; danach `python3 build.py` laufen lassen.
- DE/EN-Pattern, Design-Tokens, flache Navigation, Reveal-Failsafe und Bild-Fallback dürfen nicht brechen.
- **Verifizieren** (z. B. headless mit Playwright/Chromium): alle Seiten laden ohne JS-Fehler, **kein horizontaler Overflow** auf 390 px und 1440 px, Mobilmenü öffnet/schließt, Sprachumschalter wirkt, interne `.html`-Links zeigen alle auf existierende Dateien. JSON-LD gegen den Schema-Validator prüfen (valides JSON).
- Am Ende: kurze Zusammenfassung der Änderungen + Liste neuer Dateien.

Frag nur nach, wenn eine Entscheidung inhaltlich unklar ist — sonst triff sinnvolle Annahmen im Sinne der Marke und setz um.
