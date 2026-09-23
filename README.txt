ANDREAS KISS – Hochzeitsfotografie Innsbruck & Tirol
Mehrseitige, zweisprachige (DE/EN) Website. Fuer Claude Code: siehe CLAUDE.md.

SEITEN / DATEIEN
  index.html standesamt.html familie.html paar-portraet.html
  preise.html portfolio.html ueber-mich.html kontakt.html
  assets/site.css  assets/site.js  assets/img/  (Bilder)
  build.py         Generator (erzeugt alle HTML-Seiten)
  download-images.sh  holt die Bilder von der Live-Seite nach assets/img/
  CLAUDE.md        Projektkontext & Konventionen (fuer Claude Code)
  TASKS-SEO.md     naechste Aufgaben (SEO/Conversion-Ausbau)
  docs/            Wettbewerbsanalyse (Hintergrund)

BAUEN
  python3 build.py          # erzeugt alle HTML-Seiten neu

BILDER LOKAL (einmalig)
  bash download-images.sh   # laedt alle Bilder nach assets/img/
  Fallback: fehlt eine Datei, laedt die Seite sie automatisch von der Live-URL.

HOCHLADEN
  Alle Dateien inkl. Ordner "assets" ins Web-Root von hochzeitsfotograf.tirol.
  Startseite ist index.html.

HINWEISE
  - Aenderungen immer in build.py, dann neu bauen (generierte .html nicht direkt editieren).
  - Preise sind editierbare Richtwerte.
  - Kontaktformular oeffnet das Mailprogramm (mailto).
