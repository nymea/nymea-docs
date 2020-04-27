<script>
  import { onMount, afterUpdate, setContext } from 'svelte';

  let colsCount = 0;

  afterUpdate(() => {
    colsCount = document.querySelectorAll('.col').length;
    setContext('colsCount', colsCount);
    console.log('Row:afterUpdate()');
  });
</script>

<style>
  .row {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
</style>

<div class="row">
  <slot></slot>
</div>