<script>
  import { onMount } from 'svelte';
  import { isActive, url } from '@sveltech/routify';
  
  export let level = 0;
  export let current = undefined;
  export let children = [];

  let pages = [];

  onMount(() => {
    pages = children.filter((child) => isRoutable(children, child)).map((page) => {
      let item = {
        name: page.name.split('-').map((word) => word.substring(0, 1).toUpperCase() + word.substring(1, word.length)).join(' '),
        page
      };

      if (!page.isPage) {
        if ($isActive(page.path)) {
          item.open = true;
        } else {
          item.open = false;
        }
      }

      return item;
    });
  });

  function isRoutable(children, child) {
    return (child.isPage && !children.some((currentChild) => currentChild.path === child.path && currentChild.isDir)) || child.isDir;
  }

  function isCurrentRoute(child) {
    return child.isPage && child.path == current.path;
  }


  function toggleGroup(index) {
    pages[index].open = !pages[index].open;
  }
</script>

<style>
  .level-0 {
    border-left: 0;
    margin-left: 0; 
    padding: 3rem 3rem 3rem 1.25rem;
  }

  ul {
    border-left: 1px solid var(--silver-darken-10);
    margin-left: 0.5rem;
    padding-left: 0.75rem;
  }

  li {
    color: var(--grey-base);
  }

  li > a,
  li > span {
    display: inline-block;
  }

  li > a {
    /* color: var(--text-color); */
    color: var(--grey-base);
    /* display: inline-block; */
    padding-left: 1.75rem;
    text-decoration: none;
  }

  li > span {
    margin-left: 0.5rem;
  }

  li a[aria-current="true"],
  li span[aria-current="true"] {
    color: var(--text-color);
    font-weight: 700;
  }

  li ion-icon {
    color: var(--grey-base);
    display: inline-block;
    height: 1rem;
    width: 1rem;
    transform: translateY(0.1em) rotate(-90deg);
  }

  li.group {
    cursor: default;
  }

  li.group > div > :global(ul > li > a) {
    /* padding-left: 0.5rem; */
  }

  li.group > div {
    display: none;
  }

  li.group.open > div {
    display: block;
  }

  li.group.open > ion-icon {
    transform: translateY(0.1em) rotate(0deg);
  }

  li {
    -webkit-user-select: none; /* Chrome/Safari */        
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* IE10+ */
  }
</style>

<ul class={'level-' + level}>
  {#each pages as item, index}
    {#if item.page.isPage || item.page.path === '/documentation/overview/integrations'}
      <li>
        <a href={$url(item.page.path)} aria-current={$isActive(item.page.path)}>{item.name}</a>
      </li>
    {:else}
      <li class="group" class:open={item.open}>
        <ion-icon name="chevron-down"></ion-icon>
        <span aria-current={$isActive(item.page.path)} on:click={() => toggleGroup(index)}>{item.name}</span>
        <div>
          <svelte:self level={level + 1} current={item.page} children={item.page.children} />
        </div>
      </li>
    {/if}
  {/each}
</ul>
