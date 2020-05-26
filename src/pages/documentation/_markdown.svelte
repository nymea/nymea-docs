<script>
  import { onMount } from 'svelte';
  import { route } from '@sveltech/routify';
  import hljs from 'highlight.js/lib/core';
  import asciidoc from 'highlight.js/lib/languages/asciidoc';
  import bash from 'highlight.js/lib/languages/bash';
  import cLike from 'highlight.js/lib/languages/c-like';
  import javascript from 'highlight.js/lib/languages/javascript';
  import json from 'highlight.js/lib/languages/json';
  import python from 'highlight.js/lib/languages/python';
  import qml from 'highlight.js/lib/languages/qml';
  import xml from 'highlight.js/lib/languages/xml';

  let title = $route.api.title.split('-').map((word) => word.charAt(0).toUpperCase() + word.replace('-', ' ').slice(1)).join(' ');
  
  onMount(() => {
    hljs.registerLanguage('asciidoc', asciidoc);
    hljs.registerLanguage('bash', bash);
    hljs.registerLanguage('cLike', cLike);
    hljs.registerLanguage('javascript', javascript);
    hljs.registerLanguage('json', json);
    hljs.registerLanguage('python', python);
    hljs.registerLanguage('qml', qml);
    hljs.registerLanguage('xml', xml);

    const codeBlocks = document.querySelectorAll('pre > code');
  //   const headings = document.querySelectorAll('main h1, main h2, main h3, main h4, main h5, main h2');

    codeBlocks.forEach((codeBlock) => {
      hljs.highlightBlock(codeBlock);
    });

  //   headings.forEach((heading) => {
  //     // heading.id = encodeURIComponent(heading.innerText.toLowerCase().replace(' ', '-'));
  //     heading.id = heading.innerText.toLowerCase().replace(' ', '-');
  //     heading.setAttribute('name', heading.innerText.toLowerCase().replace(' ', '-'));
  //   });

  //   if (window.location.hash) {
  //     console.log('window.location.hash', window.location.hash, document.querySelector(window.location.hash));
  //     document.getElementById(window.location.hash.replace('#', '')).scrollIntoView(); 
  //   }
  });
</script>

<style>
  h1 {
    font-size: 3.5rem;
    font-weight: 500;
    line-height: 4.5rem;
  }
</style>

<h1>{title}</h1>
<slot />
