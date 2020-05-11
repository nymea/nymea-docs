<script>
  import Menu from './Menu.svelte';

  export let segment;
  export let base;
  export let items = [];
</script>

<style>
  /* nav {
    --header-height: 7.5rem;
    height: calc(100vh - var(--header-height));
    overflow: scroll;
    padding: 10.5rem 0 0 3rem;
  } */
</style>

<nav>
  <!-- Subnav -->
  <Menu {base} {segment} {items} />
</nav>
