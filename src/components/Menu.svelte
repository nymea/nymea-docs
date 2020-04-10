<script>
  import * as app from '@sapper/app';


  export let segment;
</script>

<style></style>

<h1><a href="/">nymea</a></h1>

{#if segment === 'getting-started'}
  <p>Getting Started</p>
{:else if segment === 'users'}
  <p>Users</p>
{:else if segment === 'developers'}
  <p>Developers</p>
  <ul>
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
          <!-- <li><a href="{segment}/plug-in-development/integration-plugins/interfaces">Interfaces</a></li> -->
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
  </ul>
{:else}
  <p>Documentation</p>
{/if}
