<script>
  import { onMount, afterUpdate, getContext } from 'svelte';

  const allowedWidths = ['5', '10', '15', '20', '25', '30', '33', '35', '40', '45', '50', '55', '60', '65', '66', '70', '75', '80', '85', '90', '95', '100', 'auto'];

  export let width;
  export let offset;

  onMount(() => {
    if (width === undefined) {
      width = '0';
    }

    if (offset === undefined) {
      offset = '0';
    }

    if (width !== '0' && !allowedWidths.includes(width)) {
      throw new Error(`Col: A width of ${width} is not allowed. Allowed values are: ${allowedWidths.join(', ')}`);
    }

    if (width !== 'auto') {
      width = width + '%';
    }

    offset = offset + '%';
  });
</script>

<style>
  .col {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    flex: 0 0 var(--width);
    margin-left: var(--offset);
  }
</style>

<div style="--width: {width}; --offset: {offset}" class="col">
  <slot></slot>
</div>