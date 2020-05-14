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
    --row-gap: 1.5rem;
  }

  .row {
    box-sizing: border-box;
    display: flex;
    flex: 0 0 100%;
    flex-direction: row;
    flex-wrap: nowrap;
    /* justify-content: space-between; */
    /* margin-left: calc((var(--row-gap) / 2) * -1); */
  }

  .row.wrap {
    flex-wrap: wrap;
  }
</style>

<div class="row" class:wrap {style}>
  <slot />
</div>
