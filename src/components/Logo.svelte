<script>
  export let height = 'auto';
  export let width = 'auto';
</script>

<style>
  img {
    height: var(--height);
    width: var(--width);
  }
</style>

<img src="logo.svg" alt="" class="logo" style="--height: {height}; --width: {width};" />
