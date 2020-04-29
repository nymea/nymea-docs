<script>
  import 'simplebar';
  import 'simplebar/dist/simplebar.css';
  import { stores } from '@sapper/app';
  import Logo from '../components/Logo.svelte';
  import Wrapper from '../components/Wrapper.svelte';
  import Header from '../components/Header.svelte';
  import Nav from '../components/Nav.svelte';
  import IntegrationsFilter from '../components/IntegrationsFilter.svelte';

  const { page } = stores();

  export let segment;

  let styles = {
    // '--background-color': 'white',
    // '--background-color-left': 'red',
    // '--background-color-right': 'green',
  };
  let hide = true;

  function toggleDrawer() {
    console.log('toggleDrawer()', hide);
    hide = !hide;
  }
</script>

<style>
  :root {
    --drawer-width: 20rem;
    --header-height: 6rem;
  }

  .wrapper {
    display: flex;
    height: 100vh;
    margin: 0 auto;
    max-width: 1680px;
    width: 100%;
  }

  .wrapper.details main {
    width: 100%;
    max-width: 60rem;
  }

  .wrapper.details .drawer {
    display: none;
  }

  /* .content,
  .drawer {
    float: left;
  } */

  .content {
    /* display: flex; */
    flex: 1 1 calc(100% - var(--drawer-width));
    height: 100vh;
    overflow: scroll;
    /* max-width: 100%; */
    /* position: relative; */
    width: 100%;
  }

  .content.drawer-open {
    width: calc(100% - var(--drawer-width));
  }
/* 
  .content.drawer-closed {
    width: 100%;
  } */

  header {
    background: linear-gradient(to bottom, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.7) 80%, rgba(255, 255, 255, 0.2));
    height: var(--header-height);
    display: flex;
    /* flex: 1 0 auto; */
    padding: 1.5rem 3rem;
    position: fixed;
    width: inherit;
    /* min-width: calc(100% - var(--drawer-width)); */
    z-index: 1;
  }

  .filter-toggle {
    background-color: #fff;
    border: 1px solid #efefef;
    border-radius: 1.5rem;
    height: 3rem;
    margin-left: auto;
    padding: 0.9rem 1rem 1.1rem;
    position: fixed;
      right: 3rem;
      top: 1.5rem;
    z-index: 2;
  }

  .filter-toggle ion-icon {
    font-size: 1rem;
  }

  main {
    /* height: 100vh; */
    /* height: calc(100vh - var(--header-height)); */
    /* margin-top: var(--header-height); */
    /* overflow: scroll; */
    padding: calc(var(--header-height) + 3rem) 3rem 3rem;
  }

  .drawer {
    background-color: #fff;
    border-left: 1px solid #efefef;
    box-shadow: 0 1px 1px rgba(0,0,0,0.11), 
              0 2px 2px rgba(0,0,0,0.11), 
              0 4px 4px rgba(0,0,0,0.11), 
              0 6px 8px rgba(0,0,0,0.11),
              0 8px 16px rgba(0,0,0,0.11);
    /* padding-left: 1.5rem; */
    position: fixed;
      bottom: 0;
      right: 0;
      top: 0;
    z-index: 2;
    /* flex: 0 0 var(--drawer-width); */
    /* margin-right: calc(var(--drawer-width) * -1); */
    width: var(--drawer-width);
  }

  .drawer.hide {
    box-shadow: none;
    margin-right: calc(var(--drawer-width) * -1);
    /* transform: translateX(var(--drawer-width)); */
  }

  .drawer.hide .filter-toggle {
    display: none;
  }

  @media (min-width: 60rem) {
    .wrapper.details .drawer {
      display: block;
    }
    .filter-toggle {
      display: none;
    }

    .content {
      width: calc(100% - var(--drawer-width));
    }

    .drawer {
      box-shadow: none;
      position: static;
    }

    .drawer.hide {
      margin-right: 0;
    }
  }

  /* .header {
    background: linear-gradient(rgb(255, 255, 255, 1), rgb(255, 255, 255, 0.9));
    backdrop-filter: blur(4px);
    position: fixed;
  } */

  /* div {
    width: 60em;
  } */
</style>

<!-- <div class="header">
  <Header>
    <Nav {segment} />
  </Header>
</div>

<div>
  <slot></slot>
</div> -->

<!-- <Wrapper sticky={true} {styles}>
  <Header border={$page.path.includes('documentation') ? true : false}>
    <Nav {segment} />
  </Header>
</Wrapper> -->

<div class="wrapper" class:details={$page.path.includes('integrations')}>
  <div class="content {hide ? 'drawer-closed' : 'drawer-open'}" data-simplebar>
    <header>
      <a href=".">
        <Logo height="3rem" />
      </a>
      {#if !$page.path.includes('integrations')}
        <div class="filter-toggle" on:click={() => toggleDrawer()}>
          <ion-icon name="funnel"></ion-icon>
        </div>
      {/if}
    </header>
    <main>
      <slot></slot>
    </main>
  </div>
  <div class="drawer" class:hide={hide}>
    <div class="filter-toggle" on:click={() => toggleDrawer()}>
      <ion-icon name="close"></ion-icon>
    </div>
    {#if !$page.path.includes('integrations')}
      <IntegrationsFilter />
    {/if}
  </div>
</div>
