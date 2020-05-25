<script>
  import { onMount } from 'svelte';
  import { route } from '@sveltech/routify';
  import ClipboardJS from 'clipboard';
  import Prism from 'prismjs';
  import 'prismjs/components/prism-bash';
  import 'prismjs/components/prism-c';
  import 'prismjs/components/prism-cpp';
  import 'prismjs/components/prism-javascript';
  import 'prismjs/components/prism-json';
  import 'prismjs/components/prism-python';
  import 'prismjs/components/prism-qml';
  import 'prismjs/components/prism-xml';
  import 'prismjs/plugins/command-line';
  import 'prismjs/plugins/toolbar/prism-toolbar';

  // QML, C++ (Qt), JSON, Python, 

  console.log('ClipboardJS', ClipboardJS);

  window.Prism = window.Prism || {};
  window.Prism.manual = true;

  console.log('$route', $route);
  let title = $route.api.title.split('-').map((word) => word.charAt(0).toUpperCase() + word.replace('-', ' ').slice(1)).join(' ');

  Prism.plugins.toolbar.registerButton('copy-to-clipboard', function (env) {
    var linkCopy = document.createElement('button');
    linkCopy.textContent = 'Copy';

    console.log('linkCopy', linkCopy);

    if (!ClipboardJS) {
      callbacks.push(registerClipboard);
    } else {
      registerClipboard();
    }

    return linkCopy;

    function registerClipboard() {
      var clip = new ClipboardJS(linkCopy, {
        'text': function () {
          console.log('test', env);
          return env.code;
        }
      });

      clip.on('success', function() {
        console.log('test - success');
        linkCopy.textContent = 'Copied!';

        resetText();
      });
      clip.on('error', function () {
        console.log('test - error');
        linkCopy.textContent = 'Press Ctrl+C to copy';

        resetText();
      });
    }

    function resetText() {
      setTimeout(function () {
        linkCopy.textContent = 'Copy';
      }, 5000);
    }
  });
  
  onMount(() => {
    const codeBlocks = document.querySelectorAll('pre > code');
    const headings = document.querySelectorAll('main h1, main h2, main h3, main h4, main h5, main h2');
    console.log('headings', headings);
    console.log('codeBlocks', codeBlocks, codeBlocks.length);
    codeBlocks.forEach((codeBlock) => {
      const languageClass = Array.from(codeBlock.classList.values()).find((value) => value.includes('language-'));
      const parentElement = codeBlock.parentElement;
      console.log('languageClass', languageClass);
      if (parentElement.tagName === 'PRE') {
        parentElement.classList.add(languageClass ? languageClass : 'language-none');
      }
      switch (languageClass) {
        case 'language-bash':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.bash, 'bash');
          break;
        case 'language-cpp':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.cpp, 'cpp');
          break;
        case 'language-javascript':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.javascript, 'javascript');
          break;
        case 'language-json':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.json, 'json');
          break;
        case 'language-python':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.python, 'python');
          break;
        case 'language-qml':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.qml, 'qml');
          break;
        case 'language-xml':
          codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.xml, 'xml');
          break;
        // default:
        //   codeBlock.innerHTML = Prism.highlight(codeBlock.textContent, Prism.languages.bash, 'bash');
      }

      console.log('codeBlock', codeBlock);
      // Prism.plugins.toolbar.hook({
      //   element: codeBlock,
      //   language: languageClass,
      //   code: codeBlock.innerText
      // });

      // codeBlock.prepend('<button>Copy</button>');
    });

    headings.forEach((heading) => {
      // heading.id = encodeURIComponent(heading.innerText.toLowerCase().replace(' ', '-'));
      heading.id = heading.innerText.toLowerCase().replace(' ', '-');
      heading.setAttribute('name', heading.innerText.toLowerCase().replace(' ', '-'));
    });

    if (window.location.hash) {
      console.log('window.location.hash', window.location.hash, document.querySelector(window.location.hash));
      document.getElementById(window.location.hash.replace('#', '')).scrollIntoView(); 
    }

    console.log('Prism.plugins.toolbar', Prism.plugins.toolbar);

    // Prism.plugins.toolbar.registerButton('hello-world', {
    //   text: 'Hello World!', // required
    //   onClick: function (env) { // optional
    //     alert('This code snippet is written in ' + env.language + '.');
    //   }
    // });
  });


  Prism.hooks.add('complete', Prism.plugins.toolbar.hook);
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
