<script>
  import Menu from './Menu.svelte';

  export let segment;
  export let base;
  export let items = [];
</script>

<style>
  nav {
    background-color: #fafafa;
    height: auto;
    min-height: 100%;
    /* margin-top: 7rem; */
    padding: 8rem 3rem;
  }
</style>

<nav>
  <!-- {base} -->
  <Menu {base} {segment} {items} />
</nav>
