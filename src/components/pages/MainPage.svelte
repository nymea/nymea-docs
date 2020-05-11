<script>
  import { stores } from '@sapper/app';
  import items from '../../routes/_menu-manual.js';
  import Col from '../grid/Col.svelte';
  import Content from '../layout/Content.svelte';
  import ContentNav from '../ContentNav.svelte';
  import Grid from '../grid/Grid.svelte';
  import Footer from '../layout/Footer.svelte';
  import Header from '../layout/Header.svelte';
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

  :global(aside:first-of-type) {
    background-color: #fafafa;
  }

  :global(aside:first-of-type .content) {
    padding: 1.5rem;
  }
</style>

<Layout>
  <Header>
    <!-- <Grid height="100%" width={{'xs': '100%', 'sm': '100%', 'md': '100%', 'lg': 'calc(100% - 40em - 1.5rem)', 'xl': 'calc(100% - 40em - 1.5rem)'}}> -->
    <Grid>
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

  <Content main>
    <slot />
  </Content>
  <!-- <Sider></Sider>
  <Sider></Sider> -->
</Layout>
