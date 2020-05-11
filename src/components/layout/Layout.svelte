<script>
  import { afterUpdate, onMount, tick } from 'svelte';
  import { createStyle } from '../utils/style.js';
  import Footer from './Footer.svelte';
  import Header from './Header.svelte';
  import Sider from './Sider.svelte';

  export let borderRadius;

  $: style = createStyle(style, {
    '--layout-border-radius': borderRadius
  });

  let parent;
  let container;
  let hidden;
  let hiddenHeader;
  let hiddenContent;
  let hiddenSiders;
  let hiddenFooter;

  function setDimensions() {
    parent = container.parentElement;

    hiddenHeader = hidden.querySelector(':scope > header');
    hiddenContent = hidden.querySelector(':scope > .content');
    hiddenSiders = hidden.querySelectorAll(':scope > aside');
    hiddenFooter = hidden.querySelector(':scope > footer');

    console.log('hiddenSiders', hiddenSiders);

    const parentBox = getComputedStyle(parent);
    const parentHeight = parent
      ? parent.clientHeight - parseFloat(parentBox.paddingTop) - parseFloat(parentBox.paddingBottom)
      : '100vh';
    const contentWrapper = container.querySelector(':scope > .content-wrapper');

    console.log('parent', parent, parent.clientHeight)

    // Move DOM elements to correct places
    if (hiddenHeader) {
      container.insertBefore(hiddenHeader, contentWrapper);
    }

    if (hiddenContent) {
      contentWrapper.append(hiddenContent);
    }

    if (hiddenSiders) {
      if (hiddenSiders[0] !== undefined) {
        contentWrapper.appendChild(hiddenSiders[0]);
      }
      
      if (hiddenSiders[1] !== undefined) {
        contentWrapper.appendChild(hiddenSiders[1]);
      }
    }

    if (hiddenFooter) {
      container.appendChild(hiddenFooter);
    }

    // Cleanup
    // hidden.remove();
    // document.querySelectorAll('.container + .hidden').forEach((element) => {
    //   if (element) {
    //     element.remove();
    //   }
    // });

    // Calculate heights and set custom properties
    const headerHeight = hiddenHeader ? hiddenHeader.offsetHeight : 0;
    const footerHeight = hiddenFooter ? hiddenFooter.offsetHeight : 0;
    const fontSize = parseFloat(getComputedStyle(document.documentElement).fontSize);

    // container.style.setProperty('--container-header-offset', (headerHeight / fontSize) + 'rem');
    // container.style.setProperty('--container-footer-offset', (footerHeight / fontSize) + 'rem');
    // container.style.setProperty('--container-height', parentHeight + 'px');
    // container.style.setProperty('--content-height', `calc(${parentHeight}px - var(--container-header-offset) - var(--container-footer-offset))`);
    // container.style.setProperty('--content-height', 'calc(100vh - var(--container-header-offset))');
  }

  onMount(async () => {
    console.log('Layout:onMount()');
    setDimensions();
    // tick();
  });

  afterUpdate(async () => {
    console.log('Layout:afterUpdate()');
    // setDimensions();
  });
</script>

<style>
  .container {
    border-radius: var(--layout-border-radius);
    display: flex;
    flex: 1;
    flex-direction: column;
    /* margin: 6rem 0; */
    /* height: auto; */
    width: 100%;
  }

  .content-wrapper {
    border-radius: var(--layout-border-radius);
    display: flex;
    flex: 1;
    flex-direction: column;
  }

  .content-wrapper :global(.content) {
    border-radius: var(--layout-border-radius);
    display: flex;
    flex-direction: column;
    flex: 1;
  }

  @media only screen and (min-width: 48em) {}

  @media only screen and (min-width: 64em) {
    .container {
      overflow-x: hidden;
    }

    .container :global(header) {
      flex: 0 0 auto;
    }

    .content-wrapper {
      flex-direction: row;
      z-index: 0;
    }

    .content-wrapper :global(.content) {
      min-width: 0;     /* Solves issue with <pre></pre> tags when there are large code blocks in there. https://weblog.west-wind.com/posts/2016/feb/15/flexbox-containers-pre-tags-and-managing-overflow */
      order: 2;
      z-index: 1;
    }

    .content-wrapper :global(aside) {
      flex-shrink: 0;
      z-index: 0;
    }

    .content-wrapper :global(aside:last-of-type) {
      order: 3;
    }

    .content-wrapper :global(aside:first-of-type) {
      order: 1;
    }

    .container :global(footer) {
      flex: 0 0 auto;
      z-index: 1;
    }
  }

  @media only screen and (min-width: 75em) {}

  @media only screen and (min-width: 105em) {}
</style>

<div class="container" {style} bind:this={container}>
  <div class="content-wrapper"></div>
</div>

<!-- Used to slot header, content, siders and footer which are moved to the right places inside .container in onMount -->
<div class="hidden" bind:this={hidden}>
  <slot></slot>
</div>
