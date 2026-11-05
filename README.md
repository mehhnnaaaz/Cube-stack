# CubeStack AI website

A static website (plain HTML, CSS and JavaScript, no framework) rebuilt from cubestackai.com.

## Pages

| URL | File |
|---|---|
| `/` | `index.html` |
| `/about/` | `about/index.html` |
| `/work/` (Our Clients) | `work/index.html` |
| `/work/zenith-skin-hair-dental-clinic-punjabi-bagh/` | case study |
| `/work/bhc-wellness-diagnostic-centre-pitampura-delhi/` | case study |
| `/work/shahi-manjil-north-york/` | case study |
| `/contact/` | `contact/index.html` |
| `/legal-pages/privacy-policy/` | `legal-pages/privacy-policy/index.html` |

The URLs match the current site, so existing Google rankings and links keep working.

## Preview on your computer

Pages link to each other with folder paths, so open them through a small local server rather than double-clicking:

```
cd cubestack-site
python3 -m http.server 8000
```

Then visit http://localhost:8000

## Publish

Upload the whole folder (except `build/`) to any static host: Netlify (drag and drop the folder), Vercel, Cloudflare Pages, GitHub Pages or Hostinger. Point cubestackai.com at it when you are ready to switch from Framer.

## Photos and videos

The pages currently load your existing photos and videos from Framer's servers. **Before cancelling Framer**, run:

```
python3 localize-media.py
```

It downloads every image and video into `assets/media/` and updates the pages to use those copies. If you regenerate the pages later with `build/build.py`, run it again.

## Contact form

The form works without a server: it turns the visitor's message into a ready-to-send WhatsApp message or email. To receive submissions directly in your inbox instead, create a free form endpoint (for example Formspree or Web3Forms) and add it to the form in `contact/index.html`:

```html
<form class="form" data-brief data-endpoint="https://formspree.io/f/YOUR_ID" novalidate>
```

## Editing content

All text lives in `build/content.py`. Edit it, then regenerate every page with:

```
python3 build/build.py
```

Styles: `assets/css/site.css` · Scripts: `assets/js/site.js` · 3D hero: `assets/js/hero3d.js`
