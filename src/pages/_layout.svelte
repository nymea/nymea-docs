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

  .header .branding {
    display: flex;
    height: var(--header-height);
  }

  .header .branding > :global(a) {
    align-self: center;
  }

  /* .footer > :global(footer > .grid > .row:first-child > .col:first-child) {
    position: relative;
  }
  
  .footer .branding {
    position: absolute;
      bottom: -2.2rem;
      left: 0;
    transform: rotate(270deg);
    transform-origin: left top;
  } */

  /* .sitemap {
    position: relative;
  }

  .sitemap::before {
    background-color: var(--silver-darken-20);
    content: "";
    display: block;
    height: calc(100% + 3rem);
    position: absolute;
      bottom: -1.5rem;
      left: -4.5rem;
    width: 1px;
  } */

  /* .sitemap nav > .menu > li > .menu {
    border-left: 1px solid var(--silver-darken-20);
    padding-left: 1.5rem;
  } */
</style>

<!-- <Layout width="80%"> -->
<Layout
  width={{'xs': '100%', 'sm': '100%', 'md': '100%', 'lg': '100%', 'xl': '100%'}}
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
  <div slot="footer" class="slot footer">
    <Footer />
  </div>
</Layout>

