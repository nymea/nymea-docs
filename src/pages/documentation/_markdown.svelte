<script>
  import TableOfContents from '../../_components/table-of-contents/TableOfContents.svelte';
  import { initCodeBlocks } from './_documentation-utils.js';

  export let title;
</script>

<style>
</style>

<h1>{title}</h1>
<TableOfContents />
<slot />
