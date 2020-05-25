<script>
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  :root {
    --header-height: 4.5rem;
    --header-border-color: var(--silver-darken-10);
  }

  .header {
    background-color: var(--silver-transparent-base);
    background-color: rgba(255, 255, 255, 0.9);
    backdrop-filter: saturate(50%) blur(4px);
    -webkit-backdrop-filter: saturate(50%) blur(4px);
    border-bottom: 1px solid var(--header-border-color);
    position: fixed;
    width: var(--layout-width);
    z-index: 2;
  }

  div,
  .header,
  .header > :global(.row > .col > [slot="branding"]),
  .header > :global(.row > .col > [slot="navigation"]),
  .header > :global(.row > .col > [slot="actions"]) {
    height: var(--header-height);
  }

  .header > :global(.row > .col > [slot="actions"]) {
    display: hidden;
  }

  @media only screen and (min-width: 48em) {
    .header > :global(.row > .col > [slot="actions"]) {
      display: block;
    }
  }
</style>

<div>
  <header class="layout header">
    <Grid width={{'xs': '100%', 'sm': '100%', 'md': '80%', 'lg': '80%', 'xl': '80%'}}>
      <Row>
        <Col span={{'xs': 1, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
          <slot name="branding" />
        </Col>
        <Col span={{'xs': 11, 'sm': 7, 'md': 7, 'lg': 7, 'xl': 7}}>
          <slot name="navigation" />
        </Col>
        <Col span={{'xs': 0, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}>
          <slot name="actions" />
        </Col>
      </Row>
    </Grid>
  </header>
</div>
