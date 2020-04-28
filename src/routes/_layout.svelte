<script>
  import { stores } from '@sapper/app';
  import Wrapper from '../components/Wrapper.svelte';
  import Header from '../components/Header.svelte';
  import Nav from '../components/Nav.svelte';

  const { page } = stores();

  export let segment;

  let styles = {
    // '--background-color': 'white',
    // '--background-color-left': 'red',
    // '--background-color-right': 'green',
  };
</script>

<style>
  div {
    min-height: 100vh;
    /* margin-top: 7.5rem; */
    /* margin: 0 1rem;
    padding: 0 2rem; */
    width: 100%;
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

<Wrapper sticky={true} {styles}>
  <Header border={$page.path.includes('documentation') ? true : false}>
    <Nav {segment} />
  </Header>
</Wrapper>

<div>
  <slot></slot>
</div>
