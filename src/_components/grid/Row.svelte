<script>
  import { createStyle } from '../utils/style.js';

  export let cols;
  export let gap;
  export let wrap = true;

  $: style = createStyle(style, {
    '--row-cols': cols,
    '--row-gap': gap,
  });
</script>

<style>
  :root {
    --row-cols-xs: 12;
    --row-cols-sm: 12;
    --row-cols-md: 12;
    --row-cols-lg: 12;
    --row-cols-xl: 12;
    --row-cols: var(--row-cols-xs);
    
    --row-gap-xs: 1.5rem;
    --row-gap-sm: 1.5rem;
    --row-gap-md: 1.5rem;
    --row-gap-lg: 1.5rem;
    --row-gap-xl: 1.5rem;
    --row-gap: var(--row-gap-xs);
  }

  .row {
    box-sizing: border-box;
    display: flex;
    flex: 0 0 100%;
    flex-direction: row;
    flex-wrap: nowrap;
    margin: 0 calc(var(--row-gap) / 2);
    
    /* justify-content: space-between; */
    /* margin-left: calc((var(--row-gap) / 2) * -1); */
  }

  /* .row:not(.wrap) {
    scrollbar-width: none;
    -ms-overflow-style: none;
  }

  .row:not(.wrap)::-webkit-scrollbar {
    height: 0;
  } */

  .row.wrap {
    flex-wrap: wrap;
  }
</style>

<div class="row" class:wrap {style}>
  <slot />
</div>
