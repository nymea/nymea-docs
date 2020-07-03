<script context="module">
  import { preferredTab } from './_store.js';
  import { derived, get, writable } from 'svelte/store';

  export const TABS = {};
</script>

<script>
  import { getContext, setContext } from 'svelte';

  let tabs = [];
  
  const selectedTab = derived(
    preferredTab,
    ($preferredTab) => {
      console.log('$selectedTab', $selectedTab);
      if ($preferredTab && tabs.find((currentTab) => currentTab.name.toLowerCase() === $preferredTab.name.toLowerCase()) !== undefined) {
        return $preferredTab;
      }
      return $selectedTab;
    }
  );

  setContext(TABS, {
    registerTabPane: (tab) => {
      tabs = [ ...tabs, tab ];

      // Autoselect first tab that gets registered
      if (tabs.length === 1) {
        preferredTab.set(tab);
      }
    },
    selectTab: (tab) => {
      preferredTab.set(tab);
    },
    preferredTab,
    selectedTab
  });

  const { selectTab } = getContext(TABS);
</script>

<style>
  button {
            appearance: none;
    -webkit-appearance: none;
    background-color: #2e3440;
    color: rgba(255, 255, 255, 0.3);
    border: 0;
    border-right: 1px solid #21252e;
    outline: 0;
    padding: var(--space-03) var(--space-07);
  }

  button:first-child {
    border-top-left-radius: 5px;
  }

  button:last-child {
    border-right: 0;
    border-top-right-radius: 5px;
  }

  button.selected {
    border-bottom: 3px solid  #21252e;
    color: var(--white);
  }

  .tabs {
    width: 100%;
  }

  .tabs-nav {
    background-color: #2e3440;
    border-bottom: 1px solid #21252e;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    display: flex;
    align-items: flex-end;
  }
</style>

<div class="tabs">
  <div class="tabs tabs-nav" role="tablist">
    {#each tabs as tab}
      <button type="button" role="tab" aria-selected={$selectedTab && $selectedTab.name.toLowerCase() === tab.name.toLowerCase()} class="tab" class:selected={$selectedTab && $selectedTab.name.toLowerCase() === tab.name.toLowerCase()} on:click={() => selectTab(tab)}>{tab.name}</button>
    {/each}
  </div>
  <div class="tabs tab-panes">
    <slot></slot>
  </div>
</div>
