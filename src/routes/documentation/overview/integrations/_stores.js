import { derived, readable, writable } from 'svelte/store';
import { meta } from './_meta.js';

function removeDuplicates(arrayWithoutDuplicates, currentItem) {
  if (!arrayWithoutDuplicates.includes(currentItem)) {
    arrayWithoutDuplicates.push(currentItem);
  }
  return arrayWithoutDuplicates;
}

function sortByName(a, b, attribute = null) {
  if (attribute) {
    return a[attribute].toLowerCase().localeCompare(b[attribute].toLowerCase());
  } else {
    return a.toLowerCase().localeCompare(b.toLowerCase());
  }
}

function filterBySearch(integration, searchInput) {
  const searchTerms = searchInput.split(' ');
  return searchTerms.reduce((found, searchTerm) => {
    return found = found
      && (
        integration.flattenedVendors.find((vendor) => vendor.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) !== undefined ||
        integration.flattenedThings.find((thing) => thing.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1) !== undefined ||
        integration.title.toLowerCase().indexOf(searchTerm.toLowerCase()) !== -1
      );
  }, true);
}

function snakeCaseToUserReadable(input) {
  return input.split('-').map((word) => word.charAt(0).toUpperCase() + word.substr(1)).join(' ');
}

function userReadableToSnakeCase(input) {
  return input.replace(' ', '-').toLowerCase();
}

function createCurrent() {
  const { subscribe, set } = writable(null);

  return {
    subscribe,
    set: (current) => set(userReadableToSnakeCase(current)),
    reset: () => set(null)
  };
}

// Search
export const searchInput = writable('');

// Categories
export const currentCategory = createCurrent();

export const categories = readable([], function start(set) {
  const categories = meta
    .reduce((categories, plugin) => {
      return categories.concat(plugin.categories);
    }, ['other'])
    .reduce((categories, category) => removeDuplicates(categories, category), [])
    .map((category) => {
      console.log('category', category);
      return {
        title: snakeCaseToUserReadable(category),
        count: category === 'other'
          ? meta.filter((integration) => integration.categories.length === 0).length
          : meta.filter((integration) => integration.categories.find((integrationCategory) => {
            return integrationCategory === category;
          })).length
      };
    })
    .sort((categoryA, categoryB) => sortByName(categoryA, categoryB, 'title'));

	set(categories);

	return function stop() {};
});

// Technologies
export const currentTechnology = createCurrent();

export const technologies = readable([], function start(set) {
  const technologies = meta
    .reduce((technologies, plugin) => {
      return technologies.concat(plugin.technology);
    }, ['other'])
    .reduce((technologies, technology) => removeDuplicates(technologies, technology), [])
    .map((technology) => {
      return {
        title: snakeCaseToUserReadable(technology),
        count: technology === 'other'
          ? meta.filter((integration) => integration.technology.length === 0).length
          : meta.filter((integration) => integration.technology.find((integrationTechnology) => {
            return integrationTechnology === technology;
          })).length
      };
    })
    .sort((technologyA, technologyB) => sortByName(technologyA, technologyB, 'title'));

	set(technologies);

  return function stop() {};
});

// Integrations
export const integrations = readable([], function start(set) {
  const integrations = meta
    .map((integration) => {
      const flattenedVendors = getVendors(integration);
      const flattenedThings = getThings(integration);
      return {
        ...integration,
        vendorsCount: flattenedVendors.length,
        flattenedVendors,
        thingsCount: flattenedThings.length,
        flattenedThings
      }
    })
    .sort((integrationA, integrationB) => integrationA.title.localeCompare(integrationB.title))

  set(integrations);

  return function stop() {};
});

export const filteredIntegrations = derived([integrations, categories, currentCategory, currentTechnology, searchInput], ([$integrations, $categories, $currentCategory, $currentTechnology, $searchInput]) => {
  const integrations = $integrations.filter((integration) => {
    return (
      $currentCategory === null
        || (
          $currentCategory === 'other'
            ? integration.categories.length === 0
            : integration.categories.find((category) => category === $currentCategory) !== undefined
        )
      )
      && (
        $currentTechnology === null
        || (
          $currentTechnology === 'other'
            ? integration.technology.length === 0
            : integration.technology.find((technology) => technology === $currentTechnology) !== undefined
        )
      );
  })
  .filter((integration) => filterBySearch(integration, $searchInput));

  return integrations;
});

// Vendors
export const vendors = readable([], function start(set) {
  const integrations = {};
  const vendors = meta
    .reduce((vendors, integration) => {
      Object.keys(integration.things).forEach((vendor) => {
        integrations[vendor] = integration;
      });
      return vendors.concat(Object.keys(integration.things));
    }, [])
    .reduce((vendors, vendor) => removeDuplicates(vendors, vendor), [])
    .map((vendor) => {
      return {
        title: snakeCaseToUserReadable(vendor),
        things: integrations[vendor].things[vendor],
        integration: integrations[vendor]
      };
    })
    .sort((vendorA, vendorB) => sortByName(vendorA, vendorB, 'title'));

	set(vendors);

	return function stop() {};
});

// Things
export const things = derived([vendors], ([$vendors]) => {
  return $vendors
    .reduce((things, vendor) => {
      return things.concat(vendor.things);
    }, [])
    .reduce((things, thing) => removeDuplicates(things, thing), [])
    .map((thing) => {
      return {
        title: snakeCaseToUserReadable(thing),
      };
    })
    .sort((thingA, thingB) => sortByName(thingA, thingB, 'title'));
});

function getVendors(plugin) {
  return Object.keys(plugin.things).map((vendor) => vendor);
}

function getThings(plugin) {
  return Object.keys(plugin.things).reduce((things, vendor) => { return things = things.concat(plugin.things[vendor]); }, []);
}