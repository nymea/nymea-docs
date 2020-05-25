<script>
  import { onMount } from 'svelte';
  import Prism from 'prismjs';
  import 'prismjs/components/prism-bash';
  import 'prismjs/components/prism-qml';
  // import 'prismjs/plugins/command-line';

  window.Prism = window.Prism || {};
  window.Prism.manual = true;
  
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

<slot />
