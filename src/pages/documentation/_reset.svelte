<script>
  import { onMount } from 'svelte';
  import { beforeUrlChange, isActive, url, layout, route, routes } from '@sveltech/routify';

  import hljs from 'highlight.js/lib/core';
  import asciidoc from 'highlight.js/lib/languages/asciidoc';
  import bash from 'highlight.js/lib/languages/bash';
  import cLike from 'highlight.js/lib/languages/c-like';
  import javascript from 'highlight.js/lib/languages/javascript';
  import json from 'highlight.js/lib/languages/json';
  import python from 'highlight.js/lib/languages/python';
  import qml from 'highlight.js/lib/languages/qml';
  import xml from 'highlight.js/lib/languages/xml';

  import Content from '../../_components/layout/Content.svelte';
  import Footer from '../../_components/layout/Footer.svelte';
  import Header from '../../_components/layout/Header.svelte';
  import Layout from '../../_components/layout/Layout.svelte';
  import Sider from '../../_components/layout/Sider.svelte';

  import Col from '../../_components/grid/Col.svelte';
  import Grid from '../../_components/grid/Grid.svelte';
  import Row from '../../_components/grid/Row.svelte';

  import Logo from '../../_components/Logo.svelte';
  import Menu from '../../_components/menu/Menu.svelte';
  import { menuOrder } from '../../_components/menu/_order.js';
  import Nav from '../../_components/Nav.svelte';
  import ExternalNav from '../../_components/ExternalNav.svelte';

  $: current = $route;
  let documentationRoute = getDocumentationRoute($route);
  let orderedLinks = [];
  let children = documentationRoute ? documentationRoute.children : [];
  let oldPath = document.location.pathname;
  let newPath = '';
  let oldHash = document.location.hash;
  let newHash = '';

  onMount(() => {
    documentationRoute = getDocumentationRoute($route);
    children = documentationRoute ? documentationRoute.children : [];

    const index = menuOrder.findIndex((orderedLink) => orderedLink.filename === documentationRoute.api.path.substring(documentationRoute.api.path.lastIndexOf('/') + 1));
    if (index !== -1 && Array.isArray(menuOrder[index + 1])) {
      orderedLinks = menuOrder[index + 1];
    }
  });

  // window.onload = function() {
  // $beforeUrlChange(() => {
    onMount(() => {
    console.log('initCodeBlocks');

    initCodeBlocks();
    
    if (window.location.hash) {
      scrollTo(window.location.hash.replace('#', ''));
    }
  });

  function initCodeBlocks() {
    hljs.registerLanguage('asciidoc', asciidoc);
    hljs.registerLanguage('bash', bash);
    hljs.registerLanguage('cLike', cLike);
    hljs.registerLanguage('javascript', javascript);
    hljs.registerLanguage('json', json);
    hljs.registerLanguage('python', python);
    hljs.registerLanguage('qml', qml);
    hljs.registerLanguage('xml', xml);

    const codeBlocks = document.querySelectorAll('pre > code');

    codeBlocks.forEach((codeBlock) => {
      hljs.highlightBlock(codeBlock);
    });
  }

  function scrollTo(id) {
    // // const id = element.id;
    // element.id = id + '-tmp';
    // window.scrollTo({top: y, behavior: 'smooth'});
    // setTimeout(() => {
      const element = document.getElementById(id);
      
      if (element) {
        const style = window.getComputedStyle(element);
        const headerHeight = parseFloat(style.getPropertyValue('--header-height').replace('rem', ''));
        const yOffset = (headerHeight + 1.5) * parseFloat(getComputedStyle(document.documentElement).fontSize);
        const y = element.getBoundingClientRect().top + window.pageYOffset - yOffset;

        // setTimeout(() => {
        //   // window.location.hash = selector;
        //   window.history.pushState({ scroll: true }, null, '#' + id);
        //   element.id = id;
        // }, 300);
        // setTimeout(() => {
          // window.scrollTo({top: y});
        // }, 0);

        // Change hash without scrolling the page
        element.id = id + '-tmp';
        window.scrollTo({top: y, behavior: 'smooth'});
        // window.location.hash = '#' + id;
        // window.history.pushState({ scroll: true }, null, '#' + id);

        setTimeout(() => {
          element.id = id;
        }, 100);
      }
    // }, 0);

    // setTimeout(() => {
    //   // window.location.hash = selector;
    //   window.history.pushState({ scroll: true }, null, '#' + id);
    //   element.id = id;
    // }, 300);
  }

  $beforeUrlChange((event, store) => {
    console.log('beforeUrlChange', event, store, event.state);

    // if (!event.state.scroll && event.url && event.url.charAt(0) === '#') {
    if (event.url && event.url.charAt(0) === '#') {
      oldHash = document.location.hash;
      scrollTo(event.url.replace(/[^a-zA-Z0-9\- ]/g, ''));

      // setTimeout(() => {
      //   console.log('TIMEOUT!!!');
      //   if(window.history.pushState) {
      //     window.history.pushState(null, null, event.url);
      //   } else {
      //     window.location.hash = event.url;
      //   }
      // }, 300);

      return false;
    }/* else if (event.state && event.state.scroll) {
      return false;
    }*/
    // else if (event.type && event.type === 'popstate') {
    //   // path changed => return true
    //   // hash changed => scrollTo & return false
    //   newPath = document.location.pathname;
    //   newHash = document.location.hash;
    //   console.log('oldPath, newPath', oldPath, newPath);
    //   console.log('oldHash, newHash', oldHash, newHash);
    //   if (newPath !== oldPath) {
    //     console.log('path changed');
    //     return true;
    //   } else if (newHash !== oldHash) {
    //     console.log('hash changed');
    //     return true;
    //   } else {
    //     return false;
    //   }
    // }

    return true;
  });

  function getDocumentationRoute(route) {
    console.log('getDocumentationRoute', route, route.parent, route.filepath, route.path);
    if (route.parent !== undefined) {
      if (route.parent.isDir && route.parent.path === '/documentation' && route.parent.children !== undefined) {
        console.log('getDocumentationRoute - 1');
        return route.parent;
      }
      console.log('getDocumentationRoute - 2');
      return getDocumentationRoute(route.parent);
    }
    console.log('getDocumentationRoute - 3');
    return null;
  }

  // getDocumentationRoute($route);
</script>

<style>
  :root {
    --header-height: 4.5rem;
    --sider-height: calc(100vh - var(--header-height));
  }

  :global(h1) {
    font-size: 3.5rem;
    font-weight: 500;
    line-height: 4.5rem;
  }

  .branding {
    display: flex;
    height: var(--header-height);
  }

  .branding > :global(a) {
    align-self: center;
  }

  .content {
    margin: 0 calc(var(--row-gap) / 2 );
  }

  .sider {
    display: none;
    padding-bottom: 3rem;
  }

  @media only screen and (min-width: 64em) {
    .sider {
      display: block;
    }
  }
</style>

<Layout
  width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}
  contentSpan={{'xs': 12, 'sm': 12, 'md': 8, 'lg': 9, 'xl': 9}}
  siderSpan={{'xs': 0, 'sm': 0, 'md': 4, 'lg': 3, 'xl': 3}}
  contentWrapperMargin="0.75rem"
  rightBackground="linear-gradient(to bottom, var(--silver-base), var(--white))"
>
  <div slot="header" class="slot header">
    <Header >
      <div slot="branding" class="branding">
        <Logo height="3rem" />
      </div>
      <div slot="navigation">
        <Nav />
      </div>
      <div slot="actions">
        <ExternalNav />
      </div>
    </Header>
  </div>
  <div slot="content" class="slot content">
    <Content main padding="3rem 0">
      <slot />
    </Content>
  </div>
  <div slot="sider" class="slot sider">
    <Sider>
      <!-- <Menu items={$layout.children} /> -->
      <Menu {current} {children} {orderedLinks} />
    </Sider>
  </div>
  <!-- <div slot="footer" class="slot">
    <Footer></Footer>
  </div> -->
</Layout>

<Footer />
