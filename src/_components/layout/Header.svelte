<script>
  import { afterUpdate, onMount } from 'svelte';
  import { createStyle } from '../utils/style.js';

  export let height = undefined;
  export let fixed = true;
  export let width = undefined;

  let div;
  let offsetWidth;
  
  $: style = createStyle(style, {
    '--header-height': height,
    '--header-width': width
  });
</script>

<style>
  :root {
    --header-background-color: var(--silver-base);
    --header-height: 6rem;
    --header-padding: 0;
    --header-width: 100%;
  }

  header {
    background-color: var(--header-background-color);
    box-sizing: content-box;
    height: var(--header-height);
    padding: var(--header-padding);
    width: 100%;
  }

  header > div {
    background-color: var(--silver-transparent-base);
    backdrop-filter: saturate(50%) blur(4px);
    -webkit-backdrop-filter: saturate(50%) blur(4px);
    border-bottom: 1px solid rgba(0, 0, 0, 0.1);
    height: var(--header-height);
    width: var(--header-width);
  }

  .fixed > div {
    position: fixed;
      top: 0;
    z-index: 1;
  }

  /* @media only screen and (min-width: 48em) { */
    header {
      /* width: calc(100% - calc(2 * var(--body-margin))); */
    }

    header,
    header > div {
      /* border-top-left-radius: var(--body-border-radius);
      border-top-right-radius: var(--body-border-radius); */
    }
  /* } */

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
<header class:fixed {style}>
  <div>
    <slot />
  </div>
</header>
