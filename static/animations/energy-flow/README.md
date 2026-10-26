# Energy in balance

A self-hosted, 12-second Hyperframes composition based on the supplied energy
system diagram, with a generic Energy Management software block and the palette
from `docs/_static/nymea.css`. All icons are vector artwork. No external requests,
fonts, API keys or build step are required to play it over HTTP(S).

## Preview and embed

Open `index.html` through the project's local preview server. Copy this whole
directory to any static web host, keeping the relative paths intact, then embed:

```html
<div style="position:relative;width:100%;padding-bottom:calc(68.75% + 64px)">
  <iframe
    src="/animations/energy-flow/index.html"
    title="Energy flows coordinated by Energy Management software"
    loading="lazy"
    style="position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:16px"
  ></iframe>
</div>
```

The extra height allows space for the controls on narrow screens. Host pages must
permit the iframe; the animation host must permit scripts and same-origin frames.
Use an image pointing to `poster.svg` on sites that prohibit JavaScript or iframes.
Direct `file://` browsing may show only the static fallback due to browser origin
restrictions; use HTTP(S) for animation playback.

The Sphinx HEMS page embeds the same file. `html_extra_path` already copies the
`static` directory into the built site, so no extension or Sphinx configuration
change is needed. Run `make html` to rebuild it. Non-HTML builders receive the SVG.

## Behaviour

- Mint streams represent electricity; lilac and blue pulses represent data and control.
- Electricity connects physical devices, not the management software or phone.
- The finite GSAP timeline is registered as `window.__timelines['energy-flow']`;
  the Hyperframes player handles seeking, playback and looping.
- Pause/play is keyboard accessible. Reduced-motion preferences disable autoplay.
- The player pauses while the document is hidden or its viewport is not visible.
- A same-origin Sphinx embed follows the site's `data-theme`. Other embeds follow
  the operating system. Select a theme manually, or use `?theme=light` / `?theme=dark`.
- Without JavaScript, or on player error, the diagram remains visible as an SVG.
- The diagram scales to its container. Labels are easiest to read at 700px or wider.

## Editing

`composition.html` contains the complete SVG scene. `composition.js` defines motion.
`poster.svg` is the matching static scene; keep it in sync when editing the artwork.
`index.html`, `embed.css` and `embed.js` provide the reusable player wrapper.
The composition is 1280 × 880 pixels and 12 seconds long.

## Bundled dependencies

- `@hyperframes/player` 0.8.152: global browser bundle from the official npm package;
  Apache-2.0, license in `vendor/HYPERFRAMES-LICENSE`.
- GSAP 3.15.0: `dist/gsap.min.js` from the official npm package; copyright and license
  notice retained in the file. Subject to the [GSAP Standard License](https://gsap.com/standard-license).

References: [Hyperframes player](https://hyperframes.heygen.com/packages/player),
[composition contract](https://hyperframes.heygen.com/guides/gsap-animation).
