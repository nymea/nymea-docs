<script>
  import { onMount } from 'svelte';
  import { categories, currentCategory, integrations, technologies, currentTechnology/*, vendors, vendorsCountAll, currentVendor*/ } from '../routes/documentation/overview/integrations/_stores.js';

  let integrationsCountAll = $integrations.length;

  onMount(() => {
    let category;
    let key;
    let value;

    const params = window.location.search.substring(1).split('&');
    
    for(let i = 0; i < params.length; i++) {
      [ key, value ] = params[i].split('=');
      console.log('CATEGORY', params[i], key, value);
      if (key === 'category') {
        console.log('CATEGORY FOUND!', key, value);
        category = value;
        break;
      }
    }

    if (category) {
      console.log('SET CATEGORY!', category);
      currentCategory.set(category);
    }
  });

  function setCategory(category) {
    if (category === null || category.title.toLowerCase().replace(' ', '-') === $currentCategory) {
      currentCategory.reset();
    } else {
      currentCategory.set(category.title);
    }
  }

  function setTechnology(technology) {
    if (technology === null || technology.title.toLowerCase().replace(' ', '-') === $currentTechnology) {
      currentTechnology.reset();
    } else {
      currentTechnology.set(technology.title);
    }
  }

  // function setVendor(vendor) {
  //    console.log('setVendor', vendor, $currentVendor);
  //   if (vendor === null || vendor === $currentVendor) {
  //     currentVendor.update((currentVendor) => currentVendor = null);
  //   } else {
  //     currentVendor.update((currentVendor) => currentVendor = vendor.title);
  //   }
  // }
</script>

<style>
  div {
    /* height: 100vh;
    overflow: scroll; */
    padding: 1.5rem;
    /* padding: 7.5rem 3rem 3rem; */
  }

  /* div > *:last-child {
    margin-bottom: 3rem;
  } */

  div > *:first-child {
    margin-top: 0;
  }

  p {
    color: #676767;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    margin: 3rem 0 1.5rem;
    text-transform: uppercase;
  }

  ul {
    list-style-type: none;
    margin: 0;
  }

  li {
    cursor: pointer;
    position: relative;
  }

  li.active {
    font-weight: 500;
  }

  li.active::before {
    background-color: #69938c;
    border-radius: 0.25rem;
    content: "";
    display: block;
    height: 0.5rem;
    position: absolute;
      left: -1rem;
      top: 0.5rem;
    width: 0.5rem;
  }

  li span {
    color: #676767;
    font-size: 0.8rem;
    font-weight: 400;
    position: relative;
      left: 0.2rem;
      top: -0.1rem;
    /* display: inline-block; */
    /* margin: -0.2rem 0 0 0.2rem; */
  }
</style>

<div>
  <p>Category</p>
  <ul>
    <li class:active={$currentCategory === null} 
        on:click={() => setCategory(null)}>
      All
      <span>{integrationsCountAll}</span>
    </li>

    {#each $categories as category}
    <li class:active={$currentCategory === category.title.toLowerCase().replace(' ', '-')}
        on:click={() => setCategory(category)}>
      {category.title}
      <span>{category.count}</span>
    </li>
    {/each}
  </ul>

  <p>Technology</p>
  <ul>
    <li class:active={$currentTechnology === null} 
        on:click={() => setTechnology(null)}>
      All
      <span>{$technologies.length}</span>
    </li>

    {#each $technologies as technology}
    <li class:active={$currentTechnology === technology.title.toLowerCase().replace(' ', '-')}
        on:click={() => setTechnology(technology)}>
      {technology.title}
      <span>{technology.count}</span>
    </li>
    {/each}
  </ul>

  <!-- <p>Vendor</p>
  <ul>
    <li class:active={$currentVendor === null} 
        on:click={() => setVendor(null)}>
      All
    </li>

    {#each $vendors as vendor}
    <li class:active={$currentVendor === vendor.title}
        on:click={() => setVendor(vendor)}>
      {vendor.title}
    </li>
    {/each}
  </ul> -->
</div>
