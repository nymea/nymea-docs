import { derived, readable, writable } from 'svelte/store';
import { meta } from './_meta.js';

function getVendors(plugin) {
  return Object.keys(plugin.things).map((vendor) => vendor);
}

function getThings(plugin) {
  return Object.keys(plugin.things).reduce((things, vendor) => { return things = things.concat(plugin.things[vendor]); }, []);
}

function search(plugin, searchTerm) {
  return plugin.flattenedVendors.find((vendor) => vendor.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) !== undefined ||
    plugin.flattenedThings.find((thing) => thing.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) !== undefined ||
    plugin.title.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1;
}

export const currentVendor = writable(null);

export const currentCategory = writable(null);

export const searchInput = writable('');

const flattenedVendors = readable([], function start(set) {
  const vendors = meta
    .reduce((vendors, integration) => {
      return vendors = vendors.concat(Object.keys(integration.things));
    }, [])
    .reduce((vendorsWithoutDuplicates, vendor) => {
      if (!vendorsWithoutDuplicates.includes(vendor)) {
        vendorsWithoutDuplicates.push(vendor);
      }
      return vendorsWithoutDuplicates;
    }, [])
    .sort((vendorA, vendorB) => vendorA.localeCompare(vendorB))
    .map((vendor) => {
      return {
        title: vendor,
        count: meta.filter((integration) => Object.keys(integration.things).find((integrationVendor) => {
          return integrationVendor === vendor;
        })).length
      };
    });

  set(vendors);

  return function stop() {};
});

export const vendors = derived([flattenedVendors, currentVendor], ([$flattenedVendors, $currentVendor]) => {
  console.log('$flattenedVendors', $flattenedVendors);
  return $flattenedVendors
    // .filter((vendor) => {
    //   console.log('vendor', vendor);
    //   return $currentVendor === null || vendor.title === $currentVendor;
    // });
});

export const vendorsCountAll = derived([flattenedVendors], ([$flattenedVendors]) => {
  return $flattenedVendors.length;
});

export const categories = readable([], function start(set) {
  const categories = meta
    .reduce((categories, plugin) => {
      return categories.concat(plugin.categories);
    }, ['other'])
    .reduce((categoriesWithoutDuplicates, category, index) => {
      if (!categoriesWithoutDuplicates.includes(category)) {
        categoriesWithoutDuplicates.push(category);
      }
      return categoriesWithoutDuplicates;
    }, [])
    .map((category) => category.split('-').map((word) => word.charAt(0).toUpperCase() + word.substr(1)).join(' '))
    .sort();

	set(categories.map((category) => {
    console.log('category', category);
    return {
      title: category,
      count: category.toLowerCase() === 'other'
        ? meta.filter((integration) => integration.categories.length === 0).length
        : meta.filter((integration) => integration.categories.find((integrationCategory) => {
          return integrationCategory.toLowerCase() === category.toLowerCase();
        })).length
    };
  }));

	return function stop() {};
});

export const integrationsCountAll = meta.length;

export const integrations = derived([categories, currentCategory, currentVendor, searchInput], ([$categories, $currentCategory, $currentVendor, $searchInput]) => {
  console.log('$categories', $categories);
  console.log('$currentCategory', $currentCategory);
  console.log('$currentVendor', $currentVendor);

  const integrations = meta.filter((integration) => {
    return (
      $currentCategory === null
        || (
          $currentCategory === 'other'
            ? integration.categories.length === 0
            : integration.categories.find((category) => category.toLowerCase() === $currentCategory) !== undefined
        )
      )
      && (
        $currentVendor === null ||
        Object.keys(integration.things).find((vendor) => vendor === $currentVendor) !== undefined
      );
  })
  .map((plugin) => {
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
  .filter((plugin) => {
    const searchTerms = $searchInput.split(' ');
    return searchTerms.reduce((found, searchTerm) => {
      return found = found && search(plugin, searchTerm);
    }, true);
  })
  .sort((integrationA, integrationB) => integrationA.title.localeCompare(integrationB.title));

  console.log('integrations', integrations.length, integrations);

  return integrations;
});
