<script>
  import { route } from '@sveltech/routify';
  import TableOfContents from '../../_components/table-of-contents/TableOfContents.svelte';
  import { initCodeBlocks } from './_documentation-utils.js';

  export let title;
</script>

<style>
</style>

{#if $route.api.path.substring(0, $route.api.path.lastIndexOf('/')) !== '/documentation/overview/integrations'}
  <h1>{title}</h1>
  <TableOfContents />
{/if}
<slot />
