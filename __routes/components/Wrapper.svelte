<script>
  export let sticky = false;
  export let styles = {};

  $: styles = {
    '--background-color': styles['--background-color'] !== undefined ? styles['--background-color'] : 'transparent',
    '--background-color-left': styles['--background-color-left'] !== undefined ? styles['--background-color-left'] : styles['--background-color'],
    '--background-color-right': styles['--background-color-right'] !== undefined ? styles['--background-color-right'] : styles['--background-color'],
    '--width': styles['width'] !== undefined ? styles['width'] : '100%',
  };
</script>

<style>
  .wrapper-outer {
    background-color: var(--background-color);
    background: linear-gradient(to right, var(--background-color-left) 0%, var(--background-color-left) 50%, var(--background-color-right) 50%);
    width: 100%;
  }

  .wrapper-inner {
    background-color: var(--background-color);
    /* display: flex;
    flex-direction: row;
    flex-wrap: wrap; */
    margin: 0 auto;
    width: var(--width);
  }
</style>

<div
  class="wrapper-outer"
  style="--background-color: {styles['--background-color']};
    --background-color-left: {styles['--background-color-left']};
    --background-color-right: {styles['--background-color-right']};
    --width: {styles['--width']};
    {sticky === true ? 'position: fixed; z-index: 1;' : ''}
    ">
  <div class="wrapper-inner">
    <slot></slot>
  </div>
</div>
