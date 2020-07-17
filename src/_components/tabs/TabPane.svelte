<script>
  import { getContext, onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import { TABS } from './Tabs.svelte';
  
  export let name = '';

  const { registerTabPane, preferredTab, selectedTab } = getContext(TABS);

  onMount(() => {
    registerTabPane({
      name
    });
  });
</script>

<style>
  .tab-pane {
    background-color: #2e3440;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
  }

  .tab-pane > :global(pre) {
    margin-top: 0;
  }
</style>

{#if $selectedTab && $selectedTab.name.toLowerCase() === name.toLowerCase()}
  <div class="tabs tab-pane" class:selected={$selectedTab && $selectedTab.name === name}>
    <slot></slot>
  </div>
{/if}
