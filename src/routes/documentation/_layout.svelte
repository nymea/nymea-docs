<script>
  // import Col from '../../components/grid/Col.svelte';
  // import Content from '../../components/Content.svelte';
  // import Footer from '../../components/Footer.svelte';
  // import Grid from '../../components/grid/Grid.svelte';
  // import Header from '../../components/Header.svelte';
  // import Layout from '../../components/Layout.svelte';
  // import Logo from '../../components/Logo.svelte';
  // import Nav from '../../components/Nav.svelte';
  // import Row from '../../components/grid/Row.svelte';
  import DocumentationPage from '../../components/pages/DocumentationPage.svelte';

  export let segment;
</script>

<style></style>

<DocumentationPage>
  <slot />
</DocumentationPage>

<!-- <slot />
<Footer>Footer: {segment}</Footer> -->
