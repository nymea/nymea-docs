<script>
  import { onMount } from 'svelte';
  import { isActive, url, layout, route, routes } from '@sveltech/routify';

  export let links = [];
  export let orderedLinkTitles = [];
  export let path = undefined;
  export let level = 0;

  let orderedLinks = [];
  
  onMount(() => {
    let orderedChildren = [];
    let orderedLinkChildren = [];

    console.log(links, orderedLinkTitles, path)

    if (path) {
      const orderedLink = path.substring(path.lastIndexOf('/') + 1);
      console.log('orderedLink', orderedLink);
      const index = orderedLinkTitles.findIndex((link) => link.filename === orderedLink);
      orderedChildren = Array.isArray(orderedLinkTitles[index + 1]) ? orderedLinkTitles[index + 1] : [];
      orderedLinkChildren = orderedChildren.filter(isLink);
    } else {
      orderedChildren = orderedLinkTitles;
      orderedLinkChildren = orderedChildren.filter(isLink);
    }

    orderedLinkChildren.forEach((currentOrderedLink) => {
      let link = links.find((link) => link.path === path + '/' + currentOrderedLink.filename);

      if (link) {
        link.title = currentOrderedLink.title;
        link.orderedLinkTitles = orderedChildren;
        orderedLinks = [ ...orderedLinks, link ];
      }
    });

    console.log('orderedLinks', orderedLinks);
  });

  function isLink(link) {
    return !Array.isArray(link);
  }
</script>

<style>
  ul {
    border-left: 1px solid var(--silver-darken-10);
    margin-bottom: 1.5rem;
    margin-left: var(--space-03);
    padding-left: var(--space-05);
  }

  .menu-1 li:last-child a,
  .menu-1 li:last-child span {
    margin-bottom: 0;
  }

  /* .menu-0,
  .group-heading + ul { */
  .menu-0 {
    border-left: 0;
    padding-left: 0;
  }

  .menu-0 {
    margin-bottom: 0;
    padding: var(--space-07);
  }

  .menu-1 {
    /* margin-bottom: 3rem; */
  }

  .group-heading {
    font-weight: 500;
    /* color: var(--menu-group-color);
    font-size: 0.8rem;
    font-weight: 400;
    letter-spacing: 0.01em;
    line-height: 1.5rem; */
    /* margin-bottom: 1.5rem; */
    /* text-transform: uppercase; */
  }

  /* li {
    padding-left: 1.5rem;
    position: relative;
  } */

  /* li::before {
    content: "\2022";
    font-size: 1.5rem;
    position: absolute;
      left: 0.75rem;
  }

  .group::before {
    content: "\203A";
  } */

  /* li {
    padding: var(--space-04) 0;
  } */

  a,
  span {
    color: var(--gray-darken-10);
    display: inline-block;
    margin-bottom: 1.5rem;
  }

  a {
    text-decoration: none;
  }

  a + ul {
    display: none;
  }

  a.active + ul {
    display: block;
  }

  .active {
    color: var(--text-color);
    /* text-decoration: underline; */
    font-weight: 700;
  }

  ion-icon {
    /* display: inline-block; */
    transform: translateX(-0.1rem) translateY(0.1rem) rotate(0deg);
    transform-origin: calc(50% - 0.1rem) calc(50% + 0.1rem);
  }

  ion-icon.open {
    color: var(--gray-base);
    transform: rotate(90deg);
  }
</style>

<ul class="menu menu-{level}">
  {#each orderedLinks as { path, title, children, parent, orderedLinkTitles }}
    {#if path !== parent.path + '/index'}
      {#if children.length === 0}
        <li>
          <a class:active={$isActive(path)} href={$url(path)}>{title}</a>
        </li>
      {:else}
        {#if children.some((child) => child.path === path + '/index')}
          <li>
            <ion-icon name="chevron-forward" class:open={$isActive(path)}></ion-icon>
            <a class:active={$isActive(path)} href={$url(path)}>{title}</a>
            <svelte:self links={children} {orderedLinkTitles} {path} level={level + 1} />
          </li>
        {:else}
          <li class="group">
            <ion-icon class="open" name="chevron-forward"></ion-icon>
            <span class="group-heading" class:active={$isActive(path)}>{title}</span>
            <svelte:self links={children} {orderedLinkTitles} {path} level={level + 1} />
          </li>
        {/if}
        <!-- <svelte:self links={children} {orderedLinkTitles} {path} level={level + 1} /> -->
      {/if}
    {/if}
  {/each}
</ul>
