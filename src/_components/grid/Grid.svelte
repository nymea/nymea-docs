<script>
  import { createStyle } from '../utils/style.js';

  export let center = true;
  export let width;

  $: style = createStyle(style, {
    '--grid-width': width
  });
</script>

<style>
  :root {
    --grid-width-xs: 100%;
    --grid-width-sm: 100%;
    --grid-width-md: 100%;
    --grid-width-lg: 100%;
    --grid-width-xl: 100%;
    --grid-width: var(--grid-width-xs);
  }

  .grid {
    box-sizing: border-box;
    /* display: flex; */
    overflow: auto;
    /* padding: 0 calc(var(--row-gap) / 2); */
    /* padding: 1.5rem; */
    width: var(--grid-width-xs);
  }

  .grid.center {
    margin-left: auto;
    margin-right: auto;
  }

  @media only screen and (min-width: 48em) {
    .grid {
      width: var(--grid-width-sm);
    }
  }

  @media only screen and (min-width: 64em) {
    .grid {
      width: var(--grid-width-md);
    }
  }

  @media only screen and (min-width: 75em) {
    .grid {
      width: var(--grid-width-lg);
    }
  }

  @media only screen and (min-width: 105em) {
    .grid {
      width: var(--grid-width-xl);
    }
  }
</style>

<div class="grid" class:center {style}>
  <slot />
</div>
