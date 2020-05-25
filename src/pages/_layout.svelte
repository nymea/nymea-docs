<script>
  import { onMount } from 'svelte';
  import { isActive, url, layout, route, routes } from '@sveltech/routify';

  import Content from '../_components/layout/Content.svelte';
  import Footer from '../_components/layout/Footer.svelte';
  import Header from '../_components/layout/Header.svelte';
  import Layout from '../_components/layout/Layout.svelte';
  import Sider from '../_components/layout/Sider.svelte';

  import Col from '../_components/grid/Col.svelte';
  import Grid from '../_components/grid/Grid.svelte';
  import Row from '../_components/grid/Row.svelte';

  import Logo from '../_components/Logo.svelte';
  import Nav from '../_components/Nav.svelte';
  import ExternalNav from '../_components/ExternalNav.svelte';
</script>

<style>
  :root {
    --header-height: 4.5rem;
    --sider-height: calc(100vh - var(--header-height));
  }

  .branding {
    display: flex;
    height: var(--header-height);
  }

  .branding > :global(a) {
    align-self: center;
  }
</style>

<!-- <Layout width="80%"> -->
<Layout
  width={{'xs': '80%', 'sm': '80%', 'md': '80%', 'lg': '80%', 'xl': '80%'}}
  contentSpan={{'xs': 12, 'sm': 12, 'md': 12, 'lg': 12, 'xl': 12}}
>
  <div slot="header" class="slot header">
    <Header >
      <div slot="branding" class="branding">
        <Logo height="3rem" />
      </div>
      <div slot="navigation">
        <Nav />
      </div>
      <div slot="actions">
        <ExternalNav />
      </div>
    </Header>
  </div>
  <div slot="content" class="slot">
    <Content main>
      <slot />
    </Content>
  </div>
  <div slot="footer" class="slot">
    <Footer>
    </Footer>
  </div>
</Layout>

