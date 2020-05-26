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

  /* .header > :global(.grid > .row > .col > [slot="branding"]),
  .header > :global(.grid > .row > .col > [slot="navigation"]),
  .header > :global(.grid > .row > .col > [slot="actions"]) {
    background-color: rgba(0, 0, 0, 0.3);
  } */

  @media only screen and (min-width: 64em) {
    .header > :global(.row > .col > [slot="actions"]) {
      display: block;
    }
  }
</style>

<div>
  <header class="layout header">
    <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
      <Row>
        <Col span={{'xs': 2, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
          <slot name="branding" />
        </Col>
        <Col span={{'xs': 10, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}}>
          <slot name="navigation" />
        </Col>
        <Col span={{'xs': 0, 'sm': 3, 'md': 3, 'lg': 3, 'xl': 3}}>
          <slot name="actions" />
        </Col>
      </Row>
    </Grid>
  </header>
</div>
