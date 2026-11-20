# Shuu — Portfolio Website

Personal portfolio of **Vo Dang Hong Duc (Shuu)**, Senior UX/UI Designer.
A lightweight static website (plain HTML + CSS, ~1.6 MB) based on the portfolio PDF.

## Structure

```
index.html            Home: hero, about, skills/tools, project list, contact
work/*.html           Case studies (TTI, Signage Platform, CONTA, Design System)
assets/style.css      All styles and design tokens (colors, fonts, spacing)
img/                  Images as WebP (full size + "-sm" for phones)
tools/build.py        Generates the HTML pages; text content lives here
tools/crop.py         Cuts images out of the portfolio PDF page renders
```

## Updating content

Edit the text in `tools/build.py`, then from the repo root run:

```
python3 tools/build.py .
```

## Hosting

Deployed on Vercel as a static site (no build step). Every merge to `main` updates the live site.
