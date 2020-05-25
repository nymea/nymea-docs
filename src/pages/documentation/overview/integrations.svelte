<script>
  // import { stores } from '@sapper/app';
  import { url } from '@sveltech/routify';
  import Tiles from '../../../_components/tiles/Tiles.svelte';
  import Tile from '../../../_components/tiles/Tile.svelte';
  import { meta } from './integrations/_meta.js';
  import { integrations, filteredIntegrations, searchInput, things, vendors } from './integrations/_stores.js';

  // const { page } = stores();

  let categoryFilter = null;
  let displayType = 'integrations';

  function search(input) {
    searchInput.update((searchInput) => searchInput = input);
  }

  function show(type) {
    displayType = type;
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
    background-color: transparent;
    border-bottom: 0;
    color: var(--text-color);
    display: block;
    text-decoration: none;
  }

  a:hover {
    background-color: transparent;
  }

  a > h3 {
    margin-top: 0;
  }

  ul {
    list-style-type: none;
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

  /* img {
    height: 3rem;
    margin-bottom: 1.5rem;
  } */
</style>

<div>
  <h1>Integrations</h1>
  <div class="search">
    <input tabindex="0" id="search" placeholder="Bose SoundTouch" bind:value={$searchInput} on:input={(event) => search(event.target.value)} />
    {#if $searchInput === ''}
      <ion-icon name="search"></ion-icon>
    {:else}
      <ion-icon name="close" on:click={() => search('')}></ion-icon>
    {/if}
  </div>
</div>

<p>nymea integrations are extensions to nymea that add functionality to connect to a specific device or service. By default nymea ships a list of most commonly used integration but there a large list of supported integrations which can be installed depending on the needs of a certain nymea setup.</p>
<p>This section shows a list of currently supported integrations. If support for a certain device or online service is not in this list, nymea can still be extended for it by developing such an integration. Please see the developers section and don't hesitate to join [our forum](https://forum.nymea.io) to meet other users and developers and help creating new integrations.</p>

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

<p class="summary">Showing <strong on:click={() => show('integrations')}>{$integrations.length} {$integrations.length === 1 ? 'integration' : 'integrations'}</strong> which {$integrations.length === 1 ? 'supports' : 'support'} <strong on:click={() => show('vendors')}>{$vendors.length} {$vendors.length === 1 ? 'vendor' : 'vendors'}</strong> and <strong on:click={() => show('things')}>{$things.length} {$things.length === 1 ? 'thing' : 'things'}</strong>.</p>

<Tiles>
  <!-- {#each enhancedPlugins as plugin} -->
  <!-- {#if displayType === 'integrations'} -->
    {#each $filteredIntegrations as integration}
      <Tile>
        <!-- <a href="{integration.readme.replace('.md', '')}"> -->
        <a href={$url('../' + integration.readme.replace('.md', ''))}>
          <!-- <img src="img/integrationlogos/{plugin.icon}" alt=""> -->
          <h3>{integration.title}</h3>
          <p>{integration.tagline}</p>
          <p class="details">{integration.vendorsCount} {integration.vendorsCount === 1 ? 'Vendor' : 'Vendors'}, {integration.thingsCount} {integration.thingsCount === 1 ? 'Thing' : 'Things'}</p>
          <ul class="icons">
            {#if integration.offline === true}
              <li>
                <ion-icon name="cloud-offline"></ion-icon>
              </li>
            {/if}
            {#if integration.stability === 'consumer'}
              <li>
                <ion-icon name="shield-checkmark"></ion-icon>
              </li>
            {/if}
          </ul>
        </a>
      </Tile>
    {/each}
  <!-- {:else if displayType === 'vendors'}
    {#each $vendors as vendor}
      <Tile>
        <a href="{$page.path}/{vendor.integration.readme.replace('.md', '')}">
          <h2>{vendor.title}</h2>
          <p>{vendor.integration.tagline}</p>
          <ul class="icons">
            {#if vendor.integration.offline === true}
              <li>
                <ion-icon name="cloud-offline"></ion-icon>
              </li>
            {/if}
            {#if vendor.integration.stability === 'consumer'}
              <li>
                <ion-icon name="shield-checkmark"></ion-icon>
              </li>
            {/if}
          </ul>
        </a>
      </Tile>
    {/each}
  {:else if displayType === 'things'}
    {#each $things as thing}
      <Tile>
        <a href="{$page.path}/{thing.integration.readme.replace('.md', '')}">
          <h2>{thing.title}</h2>
          <p>{thing.integration.tagline}</p>
          <ul class="icons">
            {#if thing.integration.offline === true}
              <li>
                <ion-icon name="cloud-offline"></ion-icon>
              </li>
            {/if}
            {#if thing.integration.stability === 'consumer'}
              <li>
                <ion-icon name="shield-checkmark"></ion-icon>
              </li>
            {/if}
          </ul>
        </a>
      </Tile>
    {/each}
  {/if} -->
</Tiles>
