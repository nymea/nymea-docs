<script>
  import { stores } from '@sapper/app';
  import Tiles from '../../../../components/Tiles.svelte';
  import Tile from '../../../../components/Tile.svelte';
  import { meta } from './_meta.js';

  const { page } = stores();

  let categoryFilter = null;
  let searchTerm;
  let plugins = meta;

  $: categories = plugins
    .reduce((categories, plugin) => {
      return categories.concat(plugin.categories);
    }, [])
    .reduce((categoriesWithoutDuplicates, category) => {
      if (!categoriesWithoutDuplicates.includes(category)) {
        categoriesWithoutDuplicates.push(category);
      }
      return categoriesWithoutDuplicates;
    }, [])
    .map((category) => category.charAt(0).toUpperCase() + category.substr(1))
    .sort();

  $: filteredPlugins = plugins.filter((plugin) => {
      console.log('plugin.categories', plugin.categories);
      console.log('filteredPlugins', plugin.categories.includes(categoryFilter));
      return categoryFilter === null || plugin.categories.includes(categoryFilter);
    })
    .sort((pluginA, pluginB) => pluginA.title.localeCompare(pluginB.title));
  
  $: offlinePlugins = filteredPlugins.filter((plugin) => plugin.offline === true);

  function setCategory(category) {
    if (category === null || category.toLowerCase() === categoryFilter) {
      categoryFilter = null;
    } else {
      categoryFilter = category.toLowerCase();
    }
  }
</script>

<style>
  a {
    display: block;
    text-decoration: none;
  }

  a > h2 {
    margin-top: 0;
  }

  ul {
    list-style-type: none;
  }

  ul.filter {
    display: flex;
    margin: 3rem 0;
  }

  ul.filter li {
    cursor: pointer;
    margin-left: 0.75rem;
  }

  ul.filter li.active {
    text-decoration: underline;
  }

  ul.filter li::before {
    content: "\00b7";
    display: inline-block;
    margin-right: 0.75rem;
  }

  ul.filter li:first-child::before {
    display: none;
  }

  ul.filter li:first-child {
    margin-left: 0;
  }

  ul.legend {
    margin: 3rem 0;
  }

  ul.icons {
    display: flex;
    /* margin-top: 1.5rem; */
    position: absolute;
      bottom: 0;
      right: 0;
  }

  ul.icons li {
    margin-left: 0.75rem;
  }

  ul.icons li:first-child {
    margin-left: 0;
  }

  a {
    height: 100%;
    padding-bottom: 3rem;
    position: relative;
  }

  a:before {
    content: '';
    float: left;
    padding-top: 100%;
  }
</style>

<h1>Integrations</h1>

<!-- <input bind:value={searchTerm} /> -->

<ul class="filter">
  <li class:active={categoryFilter === null} on:click={() =>  setCategory(null)}>All {categoryFilter === null ? '(' + plugins.length + ')' : ''}</li>
  {#each categories as category}
    <li class:active={categoryFilter === category.toLowerCase()} on:click={() =>  setCategory(category)}>{category} {categoryFilter === category.toLowerCase() ? '(' + filteredPlugins.length + ')' : ''}</li>
  {/each}
</ul>

<ul class="legend">
  <li>
    <ion-icon name="cloud-offline"></ion-icon>
    No cloud connection needed.
  </li>
  <li>
    <ion-icon name="shield-checkmark"></ion-icon>
    Official plugin used in consumer products.
  </li>
</ul>

<Tiles>
  {#each filteredPlugins as plugin}
    <Tile>
      <a href="{$page.path}/{plugin.readme.replace('.md', '')}">
        <!-- <img src="{plugin.icon}" alt=""> -->
        <h2>{plugin.title}</h2>
        <p>{plugin.tagline}</p>
        <ul class="icons">
          {#if plugin.offline === true}
            <li>
              <ion-icon name="cloud-offline"></ion-icon>
            </li>
          {/if}
          {#if plugin.stability === 'consumer'}
            <li>
              <ion-icon name="shield-checkmark"></ion-icon>
            </li>
          {/if}
        </ul>
      </a>
    </Tile>
  {/each}
</Tiles>
