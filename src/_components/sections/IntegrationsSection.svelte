<script>
  import { url } from '@sveltech/routify';
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
  import Integrations from '../Integrations.svelte';
</script>

<style>
  .integrations {
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-09) + var(--space-07)) 0 var(--space-10);
  }

  @media only screen and (min-width: 64em) {
    .integrations {
      padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    }
  }

  h2 {
    margin-bottom: var(--space-07);
  }

  h2 + p {
    color: var(--grey-base);
    font-size: 1.125rem;
    margin-bottom: var(--space-10);
  }
</style>

<section class="integrations">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}}>
        <h2>Connection talent</h2>
        <p>Connecting things to your smart home is easy and quick. See the list of available <a href={$url('/documentation/resources/integrations')}>integrations</a>.</p>
      </Col>
    </Row>
    <Integrations />
  </Grid>
</section>
