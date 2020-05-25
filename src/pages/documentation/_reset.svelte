<script>
  import { onMount } from 'svelte';
  import { isActive, url, layout, route, routes } from '@sveltech/routify';

  import Content from '../../_components/layout/Content.svelte';
  import Footer from '../../_components/layout/Footer.svelte';
  import Header from '../../_components/layout/Header.svelte';
  import Layout from '../../_components/layout/Layout.svelte';
  import Sider from '../../_components/layout/Sider.svelte';

  import Col from '../../_components/grid/Col.svelte';
  import Grid from '../../_components/grid/Grid.svelte';
  import Row from '../../_components/grid/Row.svelte';

  import Logo from '../../_components/Logo.svelte';
  import Menu from '../../_components/menu/Menu.svelte';
  import Nav from '../../_components/Nav.svelte';
  import ExternalNav from '../../_components/ExternalNav.svelte';

  console.log('$layout', $layout);
  console.log('$route', $route);
  console.log('$routes', $routes);

  $: current = $route;
  let documentationRoute = getDocumentationRoute($route);
  // $: children = $route.parent !== undefined ? $route.parent.children : [];
  let children = documentationRoute ? documentationRoute.children : [];
  $: console.log('dirs', $routes.filter((route) => !route.isPage));

  onMount(() => {
    documentationRoute = getDocumentationRoute($route);
    children = documentationRoute ? documentationRoute.children : [];
  });

  function getDocumentationRoute(route) {
    console.log('getDocumentationRoute', route, route.parent, route.filepath, route.path);
    if (route.parent !== undefined) {
      if (route.parent.isDir && route.parent.path === '/documentation' && route.parent.children !== undefined) {
        console.log('getDocumentationRoute - 1');
        return route.parent;
      }
      console.log('getDocumentationRoute - 2');
      return getDocumentationRoute(route.parent);
    }
    console.log('getDocumentationRoute - 3');
    return null;
  }

  // getDocumentationRoute($route);
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

  .sider {
    display: none;
    padding-bottom: 3rem;
  }

  @media only screen and (min-width: 48em) {
    .sider {
      display: block;
    }
  }
</style>

<Layout
  width={{'xs': '80%', 'sm': '80%', 'md': '80%', 'lg': '80%', 'xl': '80%'}}
  contentSpan={{'xs': 8, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}}
  siderSpan={{'xs': 4, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}
  contentWrapperMargin="1.5rem"
  rightBackground="linear-gradient(to bottom, var(--silver-base), var(--white))"
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
    <Content main padding="3rem 1.5rem 3rem 0">
      <slot />
    </Content>
  </div>
  <div slot="sider" class="slot sider">
    <Sider>
      <!-- <Menu items={$layout.children} /> -->
      <Menu {current} {children} />
    </Sider>
  </div>
  <div slot="footer" class="slot">
    <Footer></Footer>
  </div>
</Layout>
