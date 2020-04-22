<script>
  // This is a hack to access the generated routes: https://discordapp.com/channels/457912077277855764/473466028106579978/644369803741495311
  // TODO: Generate routes file on our own
  import { routes } from '@sapper/internal/manifest-client';
  import items from '../routes/_menu.js';
  import { onMount } from 'svelte';

  // export let items = [];
  export let segment;

  // console.log('items', items);

  $: urls = routes.map((route) => route.pattern.toString().replace(/\\|\/\^|\?\$\//g, ''));
  $: developersUrls = urls.filter((url) => {
    console.log('url', url, url.includes('/developers'));
    return url.includes('/developers');
  });

  // $: developersRoutes = routes.map((route) => {
  //   // const pattern = new RegExp(route.pattern);
  //   console.log('test route.pattern', route, pattern.test('/developers.*'))
  //   return '';
  // });

  onMount(() => {
    console.log('Menu:onMount()', routes);

    // const currentPath = window.location.pathname.substring(1);

    // document.querySelectorAll('li > a').forEach((anchor) => {
    //   if (anchor.classList.contains('active')) {
    //     anchor.classList.remove('active');
    //   }

    //   if (anchor.getAttribute('href') === currentPath) {
    //     anchor.classList.add('active');
    //   }
    // });
  });
</script>

<style>
  :root {
    --nav-list-header-color: #676767;
    --nav-item-color: #202020;
  }

  nav {
		flex-basis: 30rem;
		flex-grow: 1;
	}

  li {
    color: var(--nav-list-header-color);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    margin: 3rem 0;
    text-transform: uppercase;
  }

  li a {
    color: var(--nav-item-color);
    display: block;
    margin-bottom: 1.5rem;
  }

  li.active a {
    color: red;
  }

  li ul li {
		font-size: 1rem;
    margin: 0.75rem 0;
    letter-spacing: 0;
    text-transform: none;
  }

  li ul li a {
    display: initial;
    margin-bottom: 0;
  }
  
  a {
    text-decoration: none;
  }
</style>

<nav>
  <h1><a href="/">nymea</a></h1>

  {#if segment === 'getting-started'}
    <p>Getting Started</p>
  {:else if segment === 'users'}
    <p>Users</p>
  {:else if segment === 'developers'}
    <p>Developers</p>
    <ul>
      {#each items as item}
        {#if item.link == true}
        <li><a href="#">{item.title}</a></li>
        {:else}
        <li>{item.title}</li>
        {/if}
        <!-- {#if item.label !== undefined}
          <li>
            {item.label}
            <ul>
            {#each item.routes as route}
              <li><a href="{segment}/{item.baseRoute}/{route.route}">{route.label}</a></li>
            {/each}
            </ul>
          </li>
        {:else}
          <li><a href="{segment}/{item.basePath}">{item.basePath}</a></li>
        {/if} -->
      {/each}
    </ul>

    <!-- <ul>
      {#each developersUrls as url}
        <li><a href={url}>{url}</a></li>
      {/each}
    </ul> -->

    <!-- <ul>
      <li>
        Nymea
        <ul>
          <li><a href="{segment}/nymea/about">About</a></li>
          <li><a href="{segment}/nymea/terms-definition">Terms definition</a></li>
          <li><a href="{segment}/nymea/usage">Usage</a></li>
          <li><a href="{segment}/nymea/features">Features</a></li>
          <li><a href="{segment}/nymea/rule-engine">Rule engine</a></li>
          <li><a href="{segment}/nymea/scripting">Scripting</a></li>
          <li><a href="{segment}/nymea/interfaces">Interfaces</a></li>
          <li><a href="{segment}/nymea/configuration">Configuration</a></li>
          <li>
            <a href="{segment}/nymea/install">Install</a>
            <ul>
              <li><a href="{segment}/nymea/install/debian">Debian</a></li>
              <li><a href="{segment}/nymea/install/snap">Snap</a></li>
              <li><a href="{segment}/nymea/install/yocto">Yocto</a></li>
            </ul>  
          </li>
        </ul>
      </li>
      <li>
        Build
        <ul>
          <li><a href="{segment}/build/build-nymea">Build nymea</a></li>
          <li><a href="{segment}/build/build-configurations">Build configurations</a></li>
          <li><a href="{segment}/build/crossbuilder">Crossbuilder</a></li>
        </ul>
      </li>
      <li>
        Plug-In Development
        <ul>
          <li><a href="{segment}/plug-in-development/introduction">Introduction</a></li>
          <li><a href="{segment}/plug-in-development/build-environment">Build environment</a></li>
          <li><a href="{segment}/plug-in-development/plugin-wizard">Plugin Wizard</a></li>
          <li><a href="{segment}/plug-in-development/integration-plugins">Integration plugins</a></li>
          <ul>
            <li><a href="{segment}/plug-in-development/integration-plugins/getting-started-integration">Getting started</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/thing-setup">Things setup</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/events-actions-states">Events, actions & states</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/browsing">Browsing things</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/interfaces">Interfaces</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/plugin-json">The plugin JSON file</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/plugin-cpp">The plugin code (C++/Qt)</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/plugin-js">The plugin code (JavaScript)</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/building-testing">Building & Testing</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/tutorial-integration-cpp">Tutorial (C++/Qt)</a></li>
            <li><a href="{segment}/plug-in-development/integration-plugins/tutorial-integration-js">Tutorial (JavaScript)</a></li>
          </ul>
        </ul>
      </li>
      <li>
        Write Clients
      </li>
      <li>
        <a href="{segment}/community">Community</a>
        <ul>
          <li><a href="{segment}/community/roadmap">Roadmap</a></li>
          <li><a href="{segment}/community/changelog">Changelog</a></li>
          <li><a href="{segment}/community/contributing">Contribute</a></li>
          <li><a href="{segment}/community/license">License</a></li>
          <li><a href="{segment}/community/faq">FAQ</a></li>
        </ul>
      </li>
    </ul> -->
  {:else}
    <p>Documentation</p>
  {/if}
</nav>
