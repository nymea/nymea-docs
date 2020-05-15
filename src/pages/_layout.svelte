<script>
  import { onMount } from 'svelte';
  import { isActive, url, layout, route, routes } from '@sveltech/routify';

  import Content from '../_components/layout/Content.svelte';
  import Footer from '../_components/layout/Footer.svelte';
  import Header from '../_components/layout/Header.svelte';
  import Layout from '../_components/layout/Layout.svelte';

  import Col from '../_components/grid/Col.svelte';
  import Grid from '../_components/grid/Grid.svelte';
  import Row from '../_components/grid/Row.svelte';

  import Logo from '../_components/Logo.svelte';
  import Nav from '../_components/Nav.svelte';
</script>

<style>
  :global(body) {
    --grid-width-xs: 100%;
    --grid-width-sm: 100%;
    --grid-width-md: 100%;
    --grid-width-lg: calc(100% - 40em);
    --grid-width-xl: calc(100% - 40em);
    /* --grid-width-md: 48em;
    --grid-width-lg: 64em;
    --grid-width-xl: 75em; */
  }

  div :global(.col > .logo) {
    display: block;
    padding: 1.5rem 0;
  }

  /* div,
  div > :global(.container) {
    border-radius: var(--body-border-radius);
  }

  div > :global(.container > header),
  div > :global(.container > header > div) {
    border-top-left-radius: var(--body-border-radius);
    border-top-right-radius: var(--body-border-radius);
  }

  div > :global(.container > .content-wrapper),
  div > :global(.container > .content-wrapper > main),
  div > :global(.container > .content-wrapper > .content) {
    border-bottom-left-radius: var(--body-border-radius);
    border-bottom-right-radius: var(--body-border-radius);
  } */
</style>

<div>
  <Layout>
    <Header>
      <!-- <Grid height="100%" width={{'xs': '100%', 'sm': '100%', 'md': '100%', 'lg': 'calc(100% - 40em - 1.5rem)', 'xl': 'calc(100% - 40em - 1.5rem)'}}> -->
      <Grid>
        <Row>
          <Col middle>
            <a href={$url('/')} class="logo"><Logo height="3rem" /></a>
          </Col>
          <Col>
            <Nav />
          </Col>
        </Row>
      </Grid>
    </Header>

    <Content main>
      <slot />
    </Content>
  </Layout>
</div>
