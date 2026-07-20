#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt die statische Webseite "Persönliche Standortbestimmung".
Wird einmalig ausgeführt, um die HTML-Dateien zu generieren.
"""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

GROUPS = {
    "gestalten": {"label": "Unterricht gestalten"},
    "begleiten": {"label": "Lernende begleiten"},
    "rolle": {"label": "Rolle & Rahmen"},
}

# id, Buchstabe (EHB), Titel, Gruppe
KOMPETENZEN = [
    (1, "A", "Unterricht planen", "gestalten"),
    (2, "B", "Unterricht vorbereiten", "gestalten"),
    (3, "C", "Unterricht durchführen", "gestalten"),
    (4, "D", "Technologien in den Unterricht integrieren", "gestalten"),
    (5, "E", "Mit den Lernenden umgehen", "begleiten"),
    (6, "F", "Lernende in Lernprozessen begleiten", "begleiten"),
    (7, "G", "Lernergebnisse beurteilen", "begleiten"),
    (8, "H", "Unterricht auswerten", "gestalten"),
    (9, "I", "Im Berufsbildungssystem kooperieren", "rolle"),
    (10, "L", "Administrieren und Organisieren", "rolle"),
    (11, "M", "Die eigene Identität und die Rolle als Lehrperson übernehmen", "rolle"),
]


def filename(i):
    return f"kompetenz-{i:02d}.html"


def page_head(title):
    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
"""


def top_bar(back_href="index.html", back_label="Zur Übersicht"):
    return f"""<div class="top-bar">
  <a class="back-link" href="{back_href}">&larr; {back_label}</a>
  <span class="eyebrow">Persönliche Standortbestimmung · SG 25–27</span>
</div>
"""


# ---------- index.html ----------

def build_index():
    html = page_head("Persönliche Standortbestimmung – Übersicht")
    html += top_bar(back_href="#", back_label="Standortbestimmung")
    html += '<div class="wrap">\n'
    html += """
<section class="hero">
  <span class="eyebrow">Zwischenbilanz nach dem 1. Studienjahr · SDS-Blocktage Magglingen 2026 · SG 25–27</span>
  <h1>Ich als Lehrperson</h1>
  <p class="subtitle">Persönliche Standortbestimmung anhand der 11 Handlungskompetenzbereiche. Auf jeder Unterseite: links Ihre Kompetenzen, rechts Ihre Entwicklungspotenziale.</p>
  <div class="legend">
"""
    for key, g in GROUPS.items():
        html += f'    <span class="legend-item {key}"><span class="legend-dot"></span>{g["label"]}</span>\n'
    html += "  </div>\n</section>\n"

    for key, g in GROUPS.items():
        html += f'<section class="group-section">\n'
        html += f'  <div class="group-heading"><span class="legend-dot" style="background:var(--{key})"></span><h2>{g["label"]}</h2></div>\n'
        html += '  <div class="card-grid">\n'
        for i, letter, title, group in KOMPETENZEN:
            if group != key:
                continue
            html += f"""    <a class="card {group}" href="{filename(i)}">
      <span class="num">{i}</span>
      <h3>{title}</h3>
      <span class="letter">Handlungskompetenz {letter}</span>
    </a>
"""
        html += "  </div>\n</section>\n"

    html += """
<div class="outlook-box">
  <span class="eyebrow">Ausblick</span>
  <h2>Daran arbeite ich weiter</h2>
  <!-- PLATZHALTER: Hier später die persönlichen Schwerpunkte fürs 2. Studienjahr eintragen -->
  <p contenteditable="true">Platzhalter: Meine Schwerpunkte fürs 2. Studienjahr ...</p>
</div>
"""
    html += "</div>\n</body>\n</html>\n"
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


# ---------- Detailseiten ----------

def build_detail(idx, letter, title, group):
    i, prev_i, next_i = idx, idx - 1, idx + 1
    prev_link = f'<a href="{filename(prev_i)}">&larr; Vorherige Kompetenz</a>' if prev_i >= 1 else '<span></span>'
    next_link = f'<a href="{filename(next_i)}">Nächste Kompetenz &rarr;</a>' if next_i <= 11 else '<span></span>'
    group_label = GROUPS[group]["label"]

    html = page_head(f"{title} – Persönliche Standortbestimmung")
    html += top_bar()
    html += '<div class="wrap">\n'
    html += f"""
<div class="detail-header">
  <span class="num-badge" style="background:var(--{group})">{i}</span>
  <div>
    <span class="group-label" style="color:var(--{group})">{group_label} · Handlungskompetenz {letter}</span>
    <h1>{title}</h1>
  </div>
</div>

<div class="person-fields">
  <div><label>Name</label><div class="field-line" contenteditable="true"></div></div>
  <div><label>Beruf / Fachbereich</label><div class="field-line" contenteditable="true"></div></div>
  <div><label>Stufe / Schule</label><div class="field-line" contenteditable="true"></div></div>
  <div><label>Datum</label><div class="field-line" contenteditable="true"></div></div>
</div>

<div class="columns">
  <div class="col {group}">
    <h2>Kompetenzen</h2>
    <!-- PLATZHALTER TEXT: Hier eigene Kompetenzen zu "{title}" eintragen -->
    <div class="placeholder-text" contenteditable="true">Platzhalter für Text: Kompetenzen ...</div>
    <!-- PLATZHALTER BILD: <img src="pfad/zum/bild.jpg" alt="Beschreibung"> hier einfügen -->
    <div class="placeholder-image">Platzhalter für Bild<br>&lt;img src="..." alt="..."&gt;</div>
  </div>
  <div class="col {group}">
    <h2>Entwicklungspotenziale</h2>
    <!-- PLATZHALTER TEXT: Hier eigene Entwicklungspotenziale zu "{title}" eintragen -->
    <div class="placeholder-text" contenteditable="true">Platzhalter für Text: Entwicklungspotenziale ...</div>
    <!-- PLATZHALTER BILD: <img src="pfad/zum/bild.jpg" alt="Beschreibung"> hier einfügen -->
    <div class="placeholder-image">Platzhalter für Bild<br>&lt;img src="..." alt="..."&gt;</div>
  </div>
</div>

<div class="page-nav">
  {prev_link}
  <a class="to-overview" href="index.html">Zur Übersicht</a>
  {next_link}
</div>
"""
    html += "</div>\n</body>\n</html>\n"
    with open(os.path.join(OUT, filename(idx)), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    build_index()
    for i, letter, title, group in KOMPETENZEN:
        build_detail(i, letter, title, group)
    print("Fertig. Dateien erzeugt in:", OUT)
