<script>
  import { onMount } from 'svelte';
  import { stores } from '@sapper/app';

  const { preloading, page, session } = stores();

  export let level = 0;
  export let base = '';
  export let items = [];
  export let parents = [];
</script>

<style>
  :root {
    --nav-list-header-color: #676767;
    --nav-item-color: #202020;
  }
  ul {
    list-style-type: none;
    margin: 0 0 0 0.75rem;
  }

  ul.level-0,
  ul.level-1 {
    margin-left: 0;
  }

  ul.level-0 > li:first-child {
    margin-top: 2.25rem;
  }

  ul.level-2 {
  }

  /* ul.level-0 > li { */ 
  li.group {
    color: var(--nav-list-header-color);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    margin: 2.25rem 0 1rem;
    text-transform: uppercase;
  }

  a {
    line-height: 1.875rem;
    text-decoration: none;
  }

/* :root {
    --nav-list-header-color: #676767;
    --nav-item-color: #202020;
  } */

  /* nav {
		flex-basis: 30rem;
		flex-grow: 1;
	}

  ul li {
    color: var(--nav-list-header-color);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    margin: 3rem 0;
    text-transform: uppercase;
  } */

  /* li a {
    color: var(--nav-item-color);
    display: block;
    margin-bottom: 1.5rem;
  }

  li.active a {
    color: red;
  }

  li ul li {
		font-size: 1rem;
    margin: 0.75rem 0;
    letter-spacing: 0;
    text-transform: none;
  }

  li ul li a {
    display: initial;
    margin-bottom: 0;
  }
  
  a {
    text-decoration: none;
  } */
</style>

<!-- <nav>
  <h1><a href="/">nymea</a></h1>

  {#if segment === 'getting-started'}
    <p>Getting Started</p>
  {:else if segment === 'users'}
    <p>Users</p>
  {:else if segment === 'developers'} -->
  <!-- {#if segment === 'developers'} -->
    <!-- <p>Developers</p> -->
    <!-- basePath: {basePath} -->
    <!-- parents: {parents} -->
    <ul class="level-{level}">
      {#each items as item}
        {#if item.link == true}
        <li><a href="{base}{parents.length > 0 ? '/' + parents.join('/') : ''}{item.id !== 'index' ? '/' + item.id : ''}">{item.title}</a></li>
        {:else}
        <li class="group">{item.title}</li>
        {/if}

        {#if item.children.length > 0}
        <svelte:self {base} parents={[ ...parents, item.id ]} level={level + 1} items={item.children}/>
        {/if}
      {/each}
    </ul>
  <!-- {:else}
    <p>Documentation</p> -->
  <!-- {/if} -->
<!-- </nav> -->
