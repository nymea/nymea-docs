<script>
  import { categories, currentCategory, integrations, vendors, vendorsCountAll, currentVendor } from '../routes/documentation/overview/integrations/_stores.js';

  let integrationsCountAll = $integrations.length;

  function setCategory(category) {
    console.log('setCategory', category, $currentCategory);
    if (category === null || category.title.toLowerCase() === $currentCategory) {
      // currentCategory = null;
      currentCategory.update((currentCategory) => currentCategory = null);
    } else {
      // currentCategory = category.toLowerCase();
      currentCategory.update((currentCategory) => currentCategory = category.title.toLowerCase());
    }
  }

  function setVendor(vendor) {
     console.log('setVendor', vendor, $currentVendor);
    if (vendor === null || vendor === $currentVendor) {
      currentVendor.update((currentVendor) => currentVendor = null);
    } else {
      currentVendor.update((currentVendor) => currentVendor = vendor.title);
    }
  }
</script>

<style>
  div {
    height: 100vh;
		overflow: scroll;
    padding: 7.5rem 3rem 3rem;
  }

  div > *:last-child {
    margin-bottom: 3rem;
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
    <li class:active={$currentCategory === category.title.toLowerCase()}
        on:click={() => setCategory(category)}>
      {category.title}
      <span>{category.count}</span>
    </li>
    {/each}
  </ul>

  <p>Vendor</p>
  <ul>
    <li class:active={$currentVendor === null} 
        on:click={() => setVendor(null)}>
      All
      <!-- <span>{vendorsCountAll}</span> -->
    </li>

    {#each $vendors as vendor}
    <li class:active={$currentVendor === vendor.title}
        on:click={() => setVendor(vendor)}>
      {vendor.title}
      <!-- <span>{vendor.count}</span> -->
    </li>
    {/each}
  </ul>
</div>
