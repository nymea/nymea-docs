import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';
import copy from 'rollup-plugin-copy';
import del from 'del';
import * as path from 'path';
import { mdsvex } from 'mdsvex';

import hljs from 'highlight.js/lib/core';
import asciidoc from 'highlight.js/lib/languages/asciidoc';
import bash from 'highlight.js/lib/languages/bash';
import cLike from 'highlight.js/lib/languages/c-like';
import javascript from 'highlight.js/lib/languages/javascript';
import json from 'highlight.js/lib/languages/json';
import python from 'highlight.js/lib/languages/python';
import qml from 'highlight.js/lib/languages/qml';
import xml from 'highlight.js/lib/languages/xml';

const staticDir = 'static'
const distDir = 'dist'
const buildDir = `${distDir}/build`
const production = !process.env.ROLLUP_WATCH;
const bundling = process.env.BUNDLING || production ? 'dynamic' : 'bundle';
const shouldPrerender = (typeof process.env.PRERENDER !== 'undefined') ? process.env.PRERENDER : !!production;

del.sync(distDir + '/**');

const escape_curlies = (str) => str.replace(/[{}]/g, c => ({ '{': '&#123;', '}': '&#125;' }[c]));

function createConfig({ output, inlineDynamicImports, plugins = [] }) {
  hljs.debugMode();
  hljs.registerLanguage('asciidoc', asciidoc);
  hljs.registerLanguage('bash', bash);
  hljs.registerLanguage('cLike', cLike);
  hljs.registerLanguage('javascript', javascript);
  hljs.registerLanguage('json', json);
  hljs.registerLanguage('python', python);
  hljs.registerLanguage('qml', qml);
  hljs.registerLanguage('xml', xml);

  const transform = inlineDynamicImports ? bundledTransform : dynamicTransform;

  return {
    inlineDynamicImports,
    input: `src/main.js`,
    output: {
      name: 'app',
      sourcemap: true,
      ...output
    },
    plugins: [
      copy({
        targets: [
          { src: staticDir + '/**/!(__index.html)', dest: distDir },
          { src: `${staticDir}/__index.html`, dest: distDir, rename: '__app.html', transform },
          { src: '.htaccess', dest: distDir },
        ], copyOnce: true
      }),
      svelte({
        extensions: ['.svelte', '.md'],
        preprocess: mdsvex({
          extension: '.md',
          highlight: {
            highlighter: (code, language) => {
              const codeBlock = language
                ? hljs.highlight(language, code, true).value
                : hljs.highlightAuto(code, ['asciidoc', 'bash', 'cLike', 'javascript', 'json', 'python', 'qml', 'xml']).value;
              return `<pre class="code"><code class="language-${language} hljs">${escape_curlies(codeBlock)}</code></pre>`;
            },
          },
          layout: path.join(__dirname, './src/pages/documentation/_markdown.svelte'),
        }),
        // enable run-time checks when not in production
        dev: !production,
        hydratable: true,
        // we'll extract any component CSS out into
        // a separate file — better for performance
        css: css => {
          css.write(`${buildDir}/bundle.css`);
        }
      }),

      // If you have external dependencies installed from
      // npm, you'll most likely need these plugins. In
      // some cases you'll need additional configuration —
      // consult the documentation for details:
      // https://github.com/rollup/rollup-plugin-commonjs
      resolve({
        browser: true,
        dedupe: importee => importee === 'svelte' || importee.startsWith('svelte/')
      }),
      commonjs(),

      // If we're building for production (npm run build
      // instead of npm run dev), minify
      production && terser(),

      ...plugins
    ],
    watch: {
      clearScreen: false
    }
  }
}


const bundledConfig = {
  inlineDynamicImports: true,
  output: {
    format: 'iife',
    file: `${buildDir}/bundle.js`
  },
  plugins: [
    !production && serve(),
    !production && livereload(distDir)
  ]
}

const dynamicConfig = {
  inlineDynamicImports: false,
  output: {
    format: 'esm',
    dir: buildDir
  },
  plugins: [
    !production && livereload(distDir),
  ]
}


const configs = [createConfig(bundledConfig)]
if (bundling === 'dynamic')
  configs.push(createConfig(dynamicConfig))
if (shouldPrerender) [...configs].pop().plugins.push(prerender())
export default configs


function serve() {
  let started = false;
  return {
    writeBundle() {
      if (!started) {
        started = true;
        require('child_process').spawn('npm', ['run', 'serve'], {
          stdio: ['ignore', 'inherit', 'inherit'],
          shell: true
        });
      }
    }
  };
}

function prerender() {
  return {
    writeBundle() {
      if (shouldPrerender) {
        require('child_process').spawn('npm', ['run', 'export'], {
          stdio: ['ignore', 'inherit', 'inherit'],
          shell: true
        });
      }
    }
  }
}

function bundledTransform(contents) {
  return contents.toString().replace('__SCRIPT__', `
	<script defer src="/build/bundle.js" ></script>
	`)
}

function dynamicTransform(contents) {
  return contents.toString().replace('__SCRIPT__', `
	<script type="module" defer src="https://unpkg.com/dimport@1.0.0/dist/index.mjs?module" data-main="/build/main.js"></script>
	<script nomodule defer src="https://unpkg.com/dimport/nomodule" data-main="/build/main.js"></script>
	`)
}
