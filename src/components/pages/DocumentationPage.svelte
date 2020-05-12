<script>
  import { stores } from '@sapper/app';
  import items from '../../routes/_menu-manual.js';
  import Col from '../grid/Col.svelte';
  import Content from '../layout/Content.svelte';
  import ContentNav from '../ContentNav.svelte';
  import Footer from '../layout/Footer.svelte';
  import Grid from '../grid/Grid.svelte';
  import Header from '../layout/Header.svelte';
  import IntegrationsFilter from '../IntegrationsFilter.svelte';
  import Layout from '../layout/Layout.svelte';
  import Logo from '../Logo.svelte';
  import Nav from '../Nav.svelte';
  import Row from '../grid/Row.svelte';
  import Sider from '../layout/Sider.svelte';
  import SubNav from '../SubNav.svelte';

  const { page } = stores();

  export let segment;

  $: base = $page.path.split('/')[0] + '/' + $page.path.split('/')[1] + '/' + $page.path.split('/')[2];
  $: currentItem = items.find((item) => item.id === $page.path.split('/')[2]);
	$: segmentItems = currentItem ? currentItem.children : [];
</script>

<style>
  :global(aside:last-of-type .content-wrapper) {
    position: relative;
  }

  :global(aside:last-of-type .content-wrapper::before) {
    border-left: 1px solid #efefef;
    content: "";
    position: absolute;
      bottom: 1.5rem;
      left: 0;
      top: 1.5rem;
  }

  :global(aside:first-of-type > div) {
    /* background-color: #fafafa; */
    /* background: linear-gradient(to bottom, #fafafa, #fff); */
    /* border-right: 1px solid #efefef; */
  }

  :global(aside:first-of-type .content) {
    padding: 1.5rem;
  }

  :global(h2) {
    margin-top: 3rem;
  }

  :global(main) {
    max-width: 50em;
  }

  :global(main a) {
    background-color: rgba(159, 200, 164, 0.2);
    border-bottom: 1px solid rgba(159, 200, 164, 0.4);
    color: #202020;
    display: inline-block;
    text-decoration: none;
  }

  :global(main a:hover) {
    background-color: rgba(159, 200, 164, 0.6);
    border-color: rgba(159, 200, 164, 1);
  }
</style>

<Layout>
  <Content>
    <Layout>
      <Header width="calc(100% - 40em - 1.5rem)">
        <Grid height="100%" width={{'xs': '100%', 'sm': '100%', 'md': '100%', 'lg': '100%', 'xl': '100%'}}>
          <Row>
            <Col middle>
              <a href="." class="logo"><Logo height="3rem" /></a>
            </Col>
            <Col>
              <Nav {segment} />
            </Col>
          </Row>
        </Grid>
      </Header>

      <Content main padding="1.5rem">
        <slot />
      </Content>
    </Layout>
  </Content>

  <Sider>
    <Layout>
      <Header width="20em"></Header>
      <Content>
        <SubNav base={base} {segment} items={segmentItems} />
      </Content>
    </Layout>
  </Sider>

  <Sider>
    <Layout>
      <Header width="20em"></Header>
      <Content>
        {#if $page.path === '/documentation/overview/integrations'}
          <IntegrationsFilter />
        {:else if $page.path.includes('/documentation')}
          <ContentNav />
        {/if}
      </Content>
    </Layout>
  </Sider>
</Layout>
