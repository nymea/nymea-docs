<script>
  import { stores } from '@sapper/app';
  import items from '../routes/_menu-manual.js';
  import Col from '../components/grid/Col.svelte';
  import Content from '../components/layout/Content.svelte';
  import ContentNav from '../components/ContentNav.svelte';
  import Grid from '../components/grid/Grid.svelte';
  import Footer from '../components/layout/Footer.svelte';
  import Header from '../components/layout/Header.svelte';
  import Layout from '../components/layout/Layout.svelte';
  import Logo from '../components/Logo.svelte';
  import Nav from '../components/Nav.svelte';
  import Row from '../components/grid/Row.svelte';
  import Sider from '../components/layout/Sider.svelte';
  import SubNav from '../components/SubNav.svelte';

  const { page } = stores();

  export let segment;

  // $: currentItem = items.find((item) => item.id === segment);
  $: base = $page.path.split('/')[0] + '/' + $page.path.split('/')[1] + '/' + $page.path.split('/')[2];
  $: currentItem = items.find((item) => item.id === $page.path.split('/')[2]);
	$: segmentItems = currentItem ? currentItem.children : [];
</script>

<style>
  /* :global(aside:last-of-type .content-wrapper) {
    position: relative;
  }

  :global(aside:last-of-type .content-wrapper::before) {
    background-color: #ddd;
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

  :global(footer) {
    background-color: #aaa;
  } */
</style>

<slot />
