<script>
  import Grid from '../grid/Grid.svelte';

  export let background = 'var(--silver-base)';
  export let borderBottom = '1px solid var(--silver-darken-10)';
  export let borderTop = '1px solid var(--silver-darken-10)';
</script>

<style>
  section {
    background: var(--background);
    border-bottom: var(--border-bottom);
    border-top: var(--border-top);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-09) + var(--space-07)) 0 var(--space-10);
  }

  @media only screen and (min-width: 64em) {
    section {
      padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    }
  }
</style>

<section style="--background: {background}; --border-bottom: {borderBottom}; --border-top: {borderTop}">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <slot />
  </Grid>
</section>
