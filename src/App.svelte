<script>
  import { onMount } from 'svelte';
  import { Router, beforeUrlChange } from '@sveltech/routify';
  import { routes } from '@sveltech/routify/tmp/routes';

  let title = 'nymea';

  onMount(() => {
    setTitle(window.location.pathname);
  });

  $beforeUrlChange((event, store) => {
    if (event.url) {
      setTitle(event.url);
    } else if (event.currentTarget) {
      setTitle(event.currentTarget.location.pathname);
    }
    return true;
  });

  function setTitle(path) {
    if (path) {
      const segments = path[0] === '/' ? path.slice(1, path.length).split('/') : path.split('/');
      if (segments.length === 0 || (segments.length === 1 && segments[0] === '')) {
        title = 'nymea';
      } else if (segments.length === 1) {
        title = segments[0] + ' · nymea';
      } else if (segments.length > 1) {
        title = segments[segments.length - 1] + ' · ' + segments[0];
      }
    } else {
      title = 'nymea';
    }
  }
</script>

<svelte:head>
  <title>{title}</title>
</svelte:head>

<Router {routes} />
