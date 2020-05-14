<script>
  import { onMount } from 'svelte';
  import { isActive, url, layout, route } from "@sveltech/routify";

  import Content from '../../_components/layout/Content.svelte';
  import Footer from '../../_components/layout/Footer.svelte';
  import Header from '../../_components/layout/Header.svelte';
  import Layout from '../../_components/layout/Layout.svelte';
  import Sider from '../../_components/layout/Sider.svelte';

  import Col from '../../_components/grid/Col.svelte';
  import Grid from '../../_components/grid/Grid.svelte';
  import Row from '../../_components/grid/Row.svelte';

  import Logo from '../../_components/Logo.svelte';
  import Nav from '../../_components/Nav.svelte';

  import { orderedLinkTitles } from '../../_components/menu/_order.js';
  import Menu from '../../_components/menu/Menu.svelte';

  import { beforeUrlChange, goto } from '@sveltech/routify';

  $: path = $route.path.split('/').slice(0, 3).join('/');
  $: links = $layout.children.find((child) => child.path === path) ? $layout.children.find((child) => child.path === path).children : [];
  $: orderedLinkTitlesFromPath = findOrderedLinkTitles(orderedLinkTitles, path.substr(1));
  $: console.log('orderedLinkTitlesFromPath', orderedLinkTitlesFromPath);

  onMount(() => {
    if ($route.file === 'index.md') {
      $goto($route.api.parent.path + '/');
    } else if ($route.api.path.slice(-1) !== '/' &&
        $route.api.path.substring($route.api.path.lastIndexOf('/') + 1) !== 'index') {
      $goto($route.api.path + '/');
    }
  });

  $beforeUrlChange((event, store) => {
    if (event.url &&
        event.url.slice(-1) !== '/' &&
        event.url.substring(event.url.lastIndexOf('/') + 1) !== 'index') {
      $goto(event.url + '/');
      return false;
    }
    return true;
  });

  function findOrderedLinkTitles(orderedLinkTitles, path) {
    const pathSegments = path.split('/');
    const title = pathSegments.shift();
    const index = orderedLinkTitles.findIndex((link) => link.filename === title);

    console.log('title', title, title === undefined, path, index, pathSegments);
    console.log('orderedLinkTitles[index + 1]', orderedLinkTitles[index + 1]);

    if (pathSegments.length === 1) {
      return orderedLinkTitles[index + 1];
    }

    if (Array.isArray(orderedLinkTitles[index + 1])) {
      return findOrderedLinkTitles(orderedLinkTitles[index + 1], pathSegments.join('/'));
    }
  }
</script>

<style>
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
    <Content>
      <Layout>
        <Header width="calc(100% - 40em - 1.5rem)">
          <Grid height="100%" width={{'xs': '100%', 'sm': '100%', 'md': '100%', 'lg': '100%', 'xl': '100%'}}>
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
      </Layout>
      <Content main>
        <slot />
      </Content>
    </Content>
    <Sider>
      <Layout>
        <Header width="20em"></Header>
        <Content>
          {#if path === '/documentation/overview'}
            <Menu {links} orderedLinkTitles={orderedLinkTitlesFromPath} {path} />
          {:else if path === '/documentation/users'}
            <Menu {links} orderedLinkTitles={orderedLinkTitlesFromPath} {path} />
          {:else if path === '/documentation/developers'}
            <Menu {links} orderedLinkTitles={orderedLinkTitlesFromPath} {path} />
          {/if}
        </Content>
      </Layout>
    </Sider>
    <Sider>
      <Layout>
        <Header width="20em"></Header>
      </Layout>
    </Sider>
  </Layout>
</div>
