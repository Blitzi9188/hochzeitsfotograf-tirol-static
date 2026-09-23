# CLAUDE.md — Projektkontext für Claude Code

Diese Datei beschreibt das Projekt und die Konventionen. **Lies sie zuerst und halte dich daran.**

## Was das ist
Statische, zweisprachige (DE/EN) **mehrseitige Website** für **Andreas Kiss – Hochzeits-, Familien- & Porträtfotograf**, lokal positioniert für **Innsbruck & Tirol** (Standesamt & kleine Hochzeiten, Familie, Paar/Porträt). Domain: hochzeitsfotograf.tirol. Bewusst eigenständige Marke, getrennt von der Dolomiten-Marke „Blitzkneisser" (blitzkneisser.com).

## Architektur — WICHTIG
- Die HTML-Seiten werden **von `build.py` (Python 3) generiert**, nicht von Hand gepflegt.
- **Jede inhaltliche/strukturelle Änderung passiert in `build.py`**, danach neu bauen. Generierte `*.html` NIE direkt editieren (werden überschrieben).
- Gemeinsame Assets:
  - `assets/site.css` — Design-System (OKLCH-Tokens, Komponenten, Responsive).
  - `assets/site.js` — Sprachumschalter, Header-Scroll, Burger-Menü, Reveal-Observer (+Failsafe), Lightbox, Bild-Fallback, mailto-Formular.
- `build.py` erzeugt: `index.html`, `standesamt.html`, `familie.html`, `paar-portraet.html`, `preise.html`, `portfolio.html`, `ueber-mich.html`, `kontakt.html` sowie `download-images.sh`.

## Bauen & Verifizieren
```bash
python3 build.py          # erzeugt alle HTML-Seiten
```
Vor „fertig": **headless rendern (Playwright/Chromium)** und prüfen:
- keine JS-Fehler in der Konsole,
- **kein horizontaler Overflow** bei 390 px und 1440 px,
- Mobilmenü öffnet/schließt (Burger ab ≤1000 px), Schließen-X klickbar,
- Sprachumschalter DE/EN wirkt,
- alle internen `.html`-Links zeigen auf existierende Dateien,
- Reveal-Inhalte werden sichtbar (Failsafe), kein Inhalt bleibt „leer".

## Konventionen (nicht brechen)
- **Zweisprachigkeit:** jeder übersetzte Text als `<span class="de">…</span><span class="en">…</span>` im DOM; CSS blendet je `html[data-lang]` aus. Bei ALLEM Neuen so umsetzen (nichts per JS nachladen → auch ohne JS vollständig).
- **Design-Tokens** aus `:root` verwenden (Farben OKLCH, `--display`/`--serif` = **Jost** (elegante geometrische Sans, KEINE Serifen), `--sans` = Inter, Akzent = tiefes Tannengrün, sparsam). Keine neuen Frameworks, kein Cremeweiß/Gold/Script/Serifen/SaaS-Karten/Verlaufstext/Glassmorphism.
- **Navigation flach** (kein Dropdown): Standesamt · Familie · Paar & Porträt · Portfolio · Preise · Über mich · Kontakt. Aktive Seite via `class="active"` (siehe `acls()` in `build.py`). Header/Footer auf allen Seiten identisch.
- **Bilder:** `assets/img/DATEINAME`; `site.js` lädt bei Fehler automatisch von `https://hochzeitsfotograf.tirol/assets/uploads/` nach. `loading="lazy"`, Aspect-Ratio/`width`/`height` setzen (kein Layout-Shift), **deutscher Alt-Text**.
- **Motion:** dezent, ease-out, `prefers-reduced-motion` respektieren; Reveal nur als Verbesserung eines bereits sichtbaren Defaults (Failsafe in `site.js` behalten).
- **Barrierefreiheit:** Fokuszustände, `aria`-Attribute, Kontrast Fließtext ≥ 4.5:1.

## Marke / echte Fakten
Andreas Kiss · E-Mail foto@blitzkneisser.com · Tel/WhatsApp +43 664 3918228 · Rohracker 6, 6092 Birgitz, Tirol · Instagram @blitzkneisser · Auszeichnungen: Way Up North Awards 2024 „Best Epic Portrait", Rangefinder Magazine. Ton: ruhig, ehrlich, dokumentarisch, „ohne Inszenierung"; kurze Sätze mit Gegensatz-Hook; österreichisches Deutsch.

## Aktueller Stand
10 Seiten inkl. Preise und **Guide** (Ratgeber-Übersicht `guide.html` + Beitrag `guide-standesamt-innsbruck.html`, weitere Guides einfach über die `GUIDES`-Liste in build.py ergänzbar). Flache Navigation (8 Punkte, Guide inkl.), DE/EN, serifenlose Typografie (Jost+Inter), lokale Bilder mit Live-Fallback, Kontakt-Formular via mailto. Preise sind editierbare Richtwerte.

## Nächste Aufgaben
Siehe **`TASKS-SEO.md`** (SEO- & Conversion-Ausbau: JSON-LD, Meta/OG, sitemap/robots, Verfügbarkeits-CTA, WhatsApp, regionale Keywords, Journal/Blog). Hintergrund/Begründung in **`docs/wettbewerbsanalyse-tirol.md`**.
