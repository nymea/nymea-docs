<script>
  export let segment;
</script>

<style></style>

<h1>nymea</h1>

{#if segment === 'getting-started'}
  <p>Getting Started</p>
{:else if segment === 'users'}
  <p>Users</p>
{:else if segment === 'developers'}
  <p>Developers</p>
{:else}
  <p>Documentation</p>
{/if}
