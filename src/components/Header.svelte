<script>
  import Row from './Row.svelte';
  import Col from './Col.svelte';
  import Logo from './Logo.svelte';

  // export let segment;
  export let border = false;

  let height = '4.5rem';
</script>

<style>
  header {
    /* box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05); */
                /* 0 2px 4px rgba(0, 0, 0, 0.05), 
                0 4px 8px rgba(0, 0, 0, 0.05), 
                0 8px 16px rgba(0, 0, 0, 0.05), 
                0 16px 32px rgba(0, 0, 0, 0.05); */
    /* display: flex; */
    /* padding: 1.5rem 0; */
  }

  div {
    background-color: #fff;
    /* background: linear-gradient(to bottom, rgba(255, 255, 255, 1) 0%, rgba(255, 255, 255, 0.7) 80%, rgba(255, 255, 255, 0.2)); */
    /* backdrop-filter: blur(1px); */
    /* border-bottom: 1px solid rgba(255, 255, 255, 0.6); */
    display: flex;
    /* margin: 0 1rem; */
    padding: 1.5rem 3rem;
  }

  .content-header {
    /* border-bottom: 1px solid #efefef; */
  }

  .content-header.border {
    border-left: 1px solid #efefef;
    border-right: 1px solid #efefef;
  }

  /* h1 {
    flex-grow: 1;
    font-weight: 2rem;
    line-height: 2rem;
    margin: 0;
    padding: 1rem 0;
  } */

  a {
    color: #222;
    font-weight: 400;
    line-height: 2rem;
    text-decoration: none;
  }

  a.logo {
    flex-grow: 1;
  }

  /* a.segment {
    flex-grow: 1;
    margin-left: 3rem;
    padding: 1.4rem 0 0.6rem;
  } */
</style>

<header>
  <Row>
    <Col width="20"></Col>

    <Col width="60">
      <div class="content-header" class:border={border}>
        <a class="logo" href=".">
          <Logo {height} />
        </a>

        <slot></slot>
      </div>
    </Col>

    <Col width="20"></Col>
  </Row>
  

  <!-- <a class="segment" href="documentation">Documentation</a> -->
  <!-- <a class="segment" href=".">Main</a> -->

  <!-- <h1>
    <a aria-current='{segment === undefined ? 'page' : undefined}' href=".">nymea</a>
  </h1> -->
</header>
