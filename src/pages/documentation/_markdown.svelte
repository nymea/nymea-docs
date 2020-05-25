<script>
  import { onMount } from 'svelte';
  import { route } from '@sveltech/routify'
  import Prism from 'prismjs';
  import 'prismjs/components/prism-bash';
  import 'prismjs/components/prism-qml';
  // import 'prismjs/plugins/command-line';

  // QML, C++ (Qt), JSON, Python, 

  window.Prism = window.Prism || {};
  window.Prism.manual = true;

  let title = $route.name.split('-').map((word) => word.charAt(0).toUpperCase() + word.replace('-', ' ').slice(1)).join(' ');

  console.log('$route', $route);
  
  onMount(() => {
    const codeBlocks = document.querySelectorAll('pre > code');
    console.log('codeBlocks', codeBlocks);
    codeBlocks.forEach((codeBlock) => {
      const languageClass = Array.from(codeBlock.classList.values()).find((value) => value.includes('language-'));
      const parentElement = codeBlock.parentElement;
      console.log('languageClass', languageClass);
      if (parentElement.tagName === 'PRE') {
        parentElement.classList.add(languageClass ? languageClass : 'language-none');
      }
      switch (languageClass) {
        case 'language-qml':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.qml, 'qml');
          break;
        case 'language-bash':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.bash, 'bash');
          break;
        // default:
        //   codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.bash, 'bash');
      }
    });
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
