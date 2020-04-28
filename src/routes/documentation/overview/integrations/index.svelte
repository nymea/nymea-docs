<script>
  import { stores } from '@sapper/app';
  import Tiles from '../../../../components/Tiles.svelte';
  import Tile from '../../../../components/Tile.svelte';
  import { meta } from './_meta.js';
  import { integrations, integrationsCountAll, searchInput, vendorsCountAll } from './_stores.js';

  const { page } = stores();

  let categoryFilter = null;
  // let searchInput = '';
  let plugins = meta;

  // $: integrationsCountAll = $integrations.length;
  // $: vendorsCountAll = $integrations.reduce((vendorsCountAll, integration) => {
  //   return vendorsCountAll = vendorsCountAll + integration.vendorsCount;
  // }, 0);
  $: thingsCountAll = $integrations.reduce((thingsCountAll, integration) => {
    return thingsCountAll = thingsCountAll + integration.thingsCount;
  }, 0);

  $: console.log(searchInput);

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

  $: enhancedPlugins = filteredPlugins.map((plugin) => {
    const flattenedVendors = getVendors(plugin);
    const flattenedThings = getThings(plugin);
    return {
      ...plugin,
      vendorsCount: flattenedVendors.length,
      flattenedVendors,
      thingsCount: flattenedThings.length,
      flattenedThings
    }
  })
  // .filter((plugin) => {
  //   const searchTerms = searchInput.split(' ');
  //   return searchTerms.reduce((found, searchTerm) => {
  //     return found = found && search(plugin, searchTerm);
  //   }, true);
  // });
  
  $: offlinePlugins = filteredPlugins.filter((plugin) => plugin.offline === true);

  // function search(plugin, searchTerm) {
  //   return plugin.flattenedVendors.find((vendor) => vendor.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) !== undefined ||
  //     plugin.flattenedThings.find((thing) => thing.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) !== undefined ||
  //     plugin.title.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1;
  // }

  function search(input) {
    console.log('search', input);
    searchInput.update((searchInput) => searchInput = input);
  }

  function setCategory(category) {
    if (category === null || category.toLowerCase() === categoryFilter) {
      categoryFilter = null;
    } else {
      categoryFilter = category.toLowerCase();
    }
  }

  function getVendors(plugin) {
    return Object.keys(plugin.things).map((vendor) => vendor);
  }

  function getThings(plugin) {
    return Object.keys(plugin.things).reduce((things, vendor) => { return things = things.concat(plugin.things[vendor]); }, []);
  }
</script>

<style>
  div {
    display: flex;
    margin: 0 0 3rem;
  }

  div h1 {
    margin: 0;
  }

  div.search {
    margin: 0.5rem 0 0.5rem auto;
    position: relative;
  }

  input {
    appearance: none;
    border: 1px solid #efefef;
    border-radius: 1rem;
    font-size: 1rem;
    height: 2rem;
    line-height: 1rem;
    padding: 0.25rem 2.75rem 0.25rem 0.75rem;
  }

  input::-webkit-input-placeholder { /* Edge */
    color: #676767;
  }

  input:-ms-input-placeholder { /* Internet Explorer 10-11 */
    color: #676767;
  }

  input::placeholder {
    color: #676767;
  }

  div.search ion-icon {
    font-size: 1.125rem;
    position: absolute;
      right: 0.75rem;
      top: 0.4375rem;
  }

  p.summary {
    margin-bottom: 3rem;
  }

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
    flex-wrap: wrap;
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

  .details {
    position: absolute;
      bottom: 0;
      left: 0;
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
    /* padding: 1.5rem 1.5rem 3rem 1.5rem; */
    padding-bottom: 1.5rem;
    position: relative;
  }

  a:before {
    content: '';
    float: left;
    padding-top: 100%;
  }

  /* .supported {
    background: rgba(159, 200, 164, 1);
    background: linear-gradient(135deg, rgba(159, 200, 164, 0.9) 0%, rgba(140, 193, 182, 0.9) 100%);
    color: #fff;
    padding: 1.5rem;
    position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      top: 0;
  } */

  img {
    height: 3rem;
    margin-bottom: 1.5rem;
  }
</style>

<div>
  <h1>Integrations</h1>
  <div class="search">
    <!-- <label for="search">Search for Vendor and/or Thing</label> -->
    <input id="search" placeholder="Bose SoundTouch" bind:value={$searchInput} on:input={(event) => search(event.target.value)} />
    {#if $searchInput === ''}
      <ion-icon name="search"></ion-icon>
    {:else}
      <ion-icon name="close" on:click={() => search('')}></ion-icon>
    {/if}
  </div>
</div>

<!-- <ul class="filter">
  <li class:active={categoryFilter === null} on:click={() =>  setCategory(null)}>All {categoryFilter === null ? '(' + plugins.length + ')' : ''}</li>
  {#each categories as category}
    <li class:active={categoryFilter === category.toLowerCase()} on:click={() =>  setCategory(category)}>{category} {categoryFilter === category.toLowerCase() ? '(' + filteredPlugins.length + ')' : ''}</li>
  {/each}
</ul> -->

<ul class="legend">
  <li>
    <ion-icon name="cloud-offline"></ion-icon>
    No cloud connection needed.
  </li>
  <li>
    <ion-icon name="shield-checkmark"></ion-icon>
    Integration through official 3rd-party API.
  </li>
</ul>

<p class="summary">Showing <strong>{integrationsCountAll} {integrationsCountAll === 1 ? 'integration' : 'integrations'}</strong> which {integrationsCountAll === 1 ? 'supports' : 'support'} <strong>{$vendorsCountAll} {$vendorsCountAll === 1 ? 'vendor' : 'vendors'}</strong> and <strong>{thingsCountAll} {thingsCountAll === 1 ? 'device or service' : 'devices and services'}</strong>.</p>

<Tiles>
  <!-- {#each enhancedPlugins as plugin} -->
  {#each $integrations as plugin}
    <Tile>
      <a href="{$page.path}/{plugin.readme.replace('.md', '')}">
        <!-- <img src="img/integrationlogos/{plugin.icon}" alt=""> -->
        <h2>{plugin.title}</h2>
        <p>{plugin.tagline}</p>
        <p class="details">{plugin.vendorsCount} {plugin.vendorsCount === 1 ? 'Vendor' : 'Vendors'}, {plugin.thingsCount} {plugin.thingsCount === 1 ? 'Thing' : 'Things'}</p>
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
        <!-- <div class="supported">
          {#each Object.keys(plugin.things).map((vendor) => ({ name: vendor, things: plugin.things[vendor] })) as vendor}
            <p><strong>{vendor.name}:</strong> {vendor.things.join(', ')}</p>
          {/each}
        </div> -->
      </a>
    </Tile>
  {/each}
</Tiles>
