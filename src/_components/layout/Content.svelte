<script>
  import { createStyle } from '../utils/style.js';

  export let main = false;
  export let padding = undefined;

  $: style = createStyle(style, {
    '--content-padding': padding,
  });
</script>

<style>
  :root {
    --content-padding: 0;
    --content-padding-xs: var(--content-padding);
    --content-padding-sm: var(--content-padding);
    --content-padding-md: var(--content-padding);
    --content-padding-lg: var(--content-padding);
    --content-padding-xl: var(--content-padding);
  }
  .content {
    /* padding: 3rem 1.5rem 3rem 0; */
    padding: var(--content-padding);
  }
</style>

{#if main === true}
  <main class="layout content" {style}>
    <slot />
  </main>
{:else}
  <div class="layout content" {style}>
    <slot />
  </div>
{/if}
