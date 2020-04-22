<script>
  import Logo from './Logo.svelte';

  // export let segment;

  let height = '4.5rem';
</script>

<style>
  header {
    display: flex;
    padding: 1.5rem 3rem;
  }

  /* h1 {
    flex-grow: 1;
    font-weight: 2rem;
    line-height: 2rem;
    margin: 0;
    padding: 1rem 0;
  } */

  a {
    color: #222;
    flex-grow: 1;
    font-weight: 400;
    text-decoration: none;
  }
</style>

<header>
  <a href=".">
    <Logo {height} />
  </a>

  <!-- <h1>
    <a aria-current='{segment === undefined ? 'page' : undefined}' href=".">nymea</a>
  </h1> -->

  <slot></slot>
</header>
