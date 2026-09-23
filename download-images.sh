#!/usr/bin/env bash
# Laedt alle verwendeten Bilder von der Live-Seite nach assets/img/.
# Einmal ausfuehren:  bash download-images.sh
set -e
cd "$(dirname "$0")/assets/img"
BASE="https://hochzeitsfotograf.tirol/assets/uploads"
echo "Lade 13 Bilder ..."
curl -fSL "$BASE/About-Me-Ich.webp" -o "About-Me-Ich.webp" && echo "  ok About-Me-Ich.webp"
curl -fSL "$BASE/Blitzkneisser-After-Wedding-Dolomites-11.jpg" -o "Blitzkneisser-After-Wedding-Dolomites-11.jpg" && echo "  ok Blitzkneisser-After-Wedding-Dolomites-11.jpg"
curl -fSL "$BASE/Blitzkneisser-After-Wedding-Dolomites-3.jpg" -o "Blitzkneisser-After-Wedding-Dolomites-3.jpg" && echo "  ok Blitzkneisser-After-Wedding-Dolomites-3.jpg"
curl -fSL "$BASE/Blitzkneisser-Dolomites-Elopement-Wedding-155.jpg" -o "Blitzkneisser-Dolomites-Elopement-Wedding-155.jpg" && echo "  ok Blitzkneisser-Dolomites-Elopement-Wedding-155.jpg"
curl -fSL "$BASE/Blitzkneisser-Hochzeit-Seefeld-8.jpg" -o "Blitzkneisser-Hochzeit-Seefeld-8.jpg" && echo "  ok Blitzkneisser-Hochzeit-Seefeld-8.jpg"
curl -fSL "$BASE/Blitzkneisser-Mountain-Elopement-Instagram-27.jpg" -o "Blitzkneisser-Mountain-Elopement-Instagram-27.jpg" && echo "  ok Blitzkneisser-Mountain-Elopement-Instagram-27.jpg"
curl -fSL "$BASE/Blitzkneisser-Mountain-Elopement-Instagram-5.jpg" -o "Blitzkneisser-Mountain-Elopement-Instagram-5.jpg" && echo "  ok Blitzkneisser-Mountain-Elopement-Instagram-5.jpg"
curl -fSL "$BASE/standesamt-hochzeit-innsbruck-altstadt-paar.jpg" -o "standesamt-hochzeit-innsbruck-altstadt-paar.jpg" && echo "  ok standesamt-hochzeit-innsbruck-altstadt-paar.jpg"
curl -fSL "$BASE/standesamt-hochzeit-innsbruck-goldenes-dachl.jpg" -o "standesamt-hochzeit-innsbruck-goldenes-dachl.jpg" && echo "  ok standesamt-hochzeit-innsbruck-goldenes-dachl.jpg"
curl -fSL "$BASE/standesamt-hochzeit-innsbruck-hofgasse-paar.jpg" -o "standesamt-hochzeit-innsbruck-hofgasse-paar.jpg" && echo "  ok standesamt-hochzeit-innsbruck-hofgasse-paar.jpg"
curl -fSL "$BASE/standesamt-hochzeit-innsbruck-nordkette-paar.jpg" -o "standesamt-hochzeit-innsbruck-nordkette-paar.jpg" && echo "  ok standesamt-hochzeit-innsbruck-nordkette-paar.jpg"
curl -fSL "$BASE/standesamt-hochzeit-innsbruck-ringuebergabe.jpg" -o "standesamt-hochzeit-innsbruck-ringuebergabe.jpg" && echo "  ok standesamt-hochzeit-innsbruck-ringuebergabe.jpg"
curl -fSL "$BASE/standesamt-hochzeit-innsbruck-trausaal-kuss.jpg" -o "standesamt-hochzeit-innsbruck-trausaal-kuss.jpg" && echo "  ok standesamt-hochzeit-innsbruck-trausaal-kuss.jpg"
echo "Fertig – alle Bilder liegen jetzt in assets/img/."
