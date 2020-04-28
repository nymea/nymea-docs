<script>
  import { onMount } from 'svelte';
  import { stores } from '@sapper/app';

  const { page } = stores();

  export let level = 0;
  export let base = '';
  export let items = [];
  export let parents = [];

  $: items = items.map((item) => {
    return {
      ...item,
      url: `/${base}${parents.length > 0 ? '/' + parents.join('/') : ''}${item.id !== 'index' ? '/' + item.id : ''}`
    };
  });
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
    /* margin-top: 3rem; */
  }

  li.group {
    color: var(--nav-list-header-color);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    margin: 3rem 0 1.5rem;
    text-transform: uppercase;
  }

  a {
    line-height: 1.5rem;
    text-decoration: none;
  }

  a.active {
    text-decoration: underline;
  }
</style>

<ul class="level-{level}">
  {#each items as item}
    {#if item.link == true}
      <li><a class:active={$page.path === item.url} href="{item.url}">{item.title}</a></li>
    {:else}
      <li class="group">{item.title}</li>
    {/if}

    {#if item.children.length > 0}
      <svelte:self {base} parents={[ ...parents, item.id ]} level={level + 1} items={item.children}/>
    {/if}
  {/each}
</ul>
