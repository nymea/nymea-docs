<script>
  import { onMount } from 'svelte';
  import { route, url } from '@sveltech/routify';
  import hljs from 'highlight.js/lib/core';
  import asciidoc from 'highlight.js/lib/languages/asciidoc';
  import bash from 'highlight.js/lib/languages/bash';
  import cLike from 'highlight.js/lib/languages/c-like';
  import javascript from 'highlight.js/lib/languages/javascript';
  import json from 'highlight.js/lib/languages/json';
  import python from 'highlight.js/lib/languages/python';
  import qml from 'highlight.js/lib/languages/qml';
  import xml from 'highlight.js/lib/languages/xml';
  import TableOfContents from '../../_components/table-of-contents/TableOfContents.svelte';

  let contents = [];
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

    // const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
    // contents = [];

    // headings.forEach((heading) => {
    //   heading.id = heading.textContent.toLowerCase().replace(/\s/g, '-');
    //   console.log(heading.tagName, heading.textContent);
    //   switch (heading.tagName) {
    //     case 'H2':
    //       contents.push({
    //         text: heading.textContent,
    //         link: `${heading.id}`
    //       });
    //       break;
    //     case 'H3':
    //       if (!Array.isArray(contents[contents.length-1])) {
    //         contents.push([]);
    //       }
    //       console.log('document.location', document.location);
    //       contents[contents.length-1].push({
    //         text: heading.textContent,
    //         link: `${heading.id}`
    //       });
    //       break;
    //     // case 'h3':
    //     //   links.push(heading.textContent);
    //     //   break;
    //   }
    //   // console.log('links', JSON.stringify(links));
    // });
    // contents = [ ...contents ];

    // console.log('contents', contents);

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

<!-- <ul class="contents">
  {#each contents as content}
    <li class={"level-" + content.tagName.replace("H", "")}>{content.innerText}</li>
  {/each}
</ul> -->

<!-- <div>
  {#if contents.length > 0}
    <p>Contents</p>
  {/if}
  <ul>
    {#each contents as link}
      {#if Array.isArray(link)}
      <ul class="inset">
        {#each link as sublink} -->
          <!-- <li><a class={currentHeading && currentHeading.id === sublink.link ? 'active' : ''} href="{$page.path}#{sublink.link}">{sublink.text}</a></li> -->
          <!-- <li><a href={$url("#" + sublink.link)}>{sublink.text}</a></li>
        {/each}
      </ul>
      {:else} -->
      <!-- <li><a class={currentHeading && currentHeading.id === link.link ? 'active' : ''} href="{$page.path}#{link.link}">{link.text}</a></li> -->
      <!-- <li><a href={$url("#" + link.link)}>{link.text}</a></li>
      {/if}
    {/each}
  </ul>
</div> -->

<TableOfContents />

<slot />
