<script>
  import { afterUpdate, onMount } from 'svelte';
  import { createStyle } from '../utils/style.js';

  // export let width = 'auto';
  export let width;

  let div;
  let offsetWidth;
  
  $: style = createStyle(style, {
    // '--header-width': width === 'auto' ? offsetWidth + 'px' : width
    '--header-width': width
  });

  // onMount(() => {
  //   // const div = document.querySelector('header > div');
  //   console.log('header - mount', div);
  //   if (div) {
  //     console.log('header - mount', div.offsetWidth);
  //   }
  // });

  // afterUpdate(() => {
  //   // const div = document.querySelector('header > div');
  //   console.log('header - after update', div);
  //   if (div) {
  //     console.log('header - after update', div.offsetWidth);
  //   }
  // });
</script>

<style>
  :root {
    --header-background-color: var(--silver-base);
    --header-height: 6rem;
    --header-padding: 0;
    --header-width: calc(100% - 1.5rem);;
  }

  header {
    background-color: var(--header-background-color);
    box-sizing: content-box;
    height: var(--header-height);
    padding: var(--header-padding);
    width: calc(100% - 1.5rem);
  }

  header > div {
    /* background-color: inherit; */
    /* background-color: rgba(255, 255, 255, 0.9); */
    background-color: var(--silver-transparent-base);
    backdrop-filter: saturate(50%) blur(4px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    border-top-left-radius: var(--body-border-radius);
    border-top-right-radius: var(--body-border-radius);
    height: var(--header-height);
    position: fixed;
    width: inherit;
    z-index: 2;
  }

  @media only screen and (min-width: 48em) {}

  @media only screen and (min-width: 64em) {
    header {
      width: 100%;
    }

    header > div {
      /* border-top-left-radius: 0;
      border-top-right-radius: 0; */
      width: var(--header-width);
    }
  }

  @media only screen and (min-width: 75em) {}

  @media only screen and (min-width: 105em) {}
</style>

<!-- <header bind:offsetWidth={offsetWidth} {style}>
  <div bind:this={div}> -->
<header {style}>
  <div>
    <slot />
  </div>
</header>
