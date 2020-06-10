<script>
  import Grid from '../grid/Grid.svelte';
</script>

<style>
  .highlight {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: 0 var(--space-07);
    padding: calc(var(--space-09) + var(--space-07)) 0 var(--space-10);
  }

  .highlight > :global(.grid) {
    overflow: visible;
  }

  @media only screen and (min-width: 64em) {
    .highlight {
      padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    }
  }

  .highlight-wrapper {
    background: linear-gradient(145deg, var(--white), var(--silver-base));
    border: 1px solid var(--white);
    border-radius: 10px;
    /* background: #ffffff; */
    box-shadow:  10px 10px 20px rgba(217, 217, 217, 0.8),
                -10px -10px 20px rgba(255, 255, 255, 0.6);
    padding: var(--space-09) 0;
    overflow-x: hidden;
    position: relative;
      /* top: calc(-1 * var(--space-10)); */
    z-index: 1;
  }

  @media only screen and (min-width: 64em) {
    .highlight-wrapper {
      box-shadow:  30px 30px 60px rgba(217, 217, 217, 0.8),
                  -30px -30px 60px rgba(255, 255, 255, 0.6);
    }
  }
</style>

<section class="highlight">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <div class="highlight-wrapper">
      <slot />
    </div>
  </Grid>
</section>
