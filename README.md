# CubeStack AI website

A static, multi-page site for CubeStack AI, styled to the CubeStack Brand Guidelines 2026:
black and white leading, violet `#7C3AED` and electric green `#B6FF00` as accents, Anton and Clash Grotesk type.

## Pages
- `index.html`: home page (film hero, particle "stack", cursor reveal, unfolding services cube, AI demo, AI visibility score, city map grids, before/after slider, case studies, testimonials, FAQ)
- `about/index.html`: About page (mission, impact, story, who we work for, values, founders, process, archetypes, FAQ)

## Open it
Opening `index.html` directly works, but a local server is best:

    python3 -m http.server 8000
    # then visit http://localhost:8000

To publish, upload the whole folder to GitHub Pages, Netlify or any static host. `.nojekyll` is included for GitHub Pages.

## Images from cubestackai.com
Photos (team, clients, services, testimonials) load from the same Framer CDN your current site uses.
To keep local copies in the project instead, run this once on a computer with internet:

    python3 tools/localize_images.py

## Editing
Header, menu and footer are shared. Edit page content in `build/pages/*.html`, then rebuild:

    python3 build/build.py

Styles: `assets/css/site.css`. Behaviour: `assets/js/core.js` (all pages), `home.js`, `about.js`.

## Assets
- `assets/video/`: your hero film (`cubestack-film.mp4`, 720p, with sound), muted hero loops (desktop and phone) and posters
- `assets/brand/`: logo, favicons and glass renders taken from the brand book

Sound is off until the visitor chooses "Enter with sound". Reduced-motion settings are respected.
