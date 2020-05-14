<script>
  import { createStyle } from '../utils/style.js';

  export let scroll = false;
  export let main = false;
  export let padding;

  $: style = createStyle(style, {
    '--content-padding': padding
  });
</script>

<style>
  :root {
    --content-background-color: #fafafa;
    --content-padding: 0;
  }

  main {
    padding: var(--space-07);
    /* padding: var(--content-padding); */
    /* background-color: var(--content-background-color); */
    /* border-top-left-radius: var(--layout-border-radius);
    border-top-right-radius: var(--layout-border-radius); */
  }

  /* .content {
    padding: var(--content-padding);
  }

  .scroll {
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
  } */
</style>

{#if main === true}
  <main class="content" class:scroll {style}>
    <slot />
  </main>
{:else}
  <div class="content" class:scroll {style}>
    <slot />
  </div>
{/if}
