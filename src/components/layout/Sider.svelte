<script>
  export let fixed = true;
  export let scroll = true;
</script>

<style>
  @media screen and (min-width: 501px) {
    aside {
      width: 20em;
    }

    .scroll {
      overflow: hidden;
    }

    .fixed {
      box-sizing: content-box;
      /* height: calc(100vh - 1.5rem - 6rem); */
      height: calc(100vh - 1.5rem);
      margin-right: -999em;
      padding-right: 999em;
      overflow-x: hidden;
      overflow-y: scroll;
      position: fixed;
      width: 20em;
      /* z-index: 0; */
    }
  }

  /* :root {
    --sider-height: 100%;
    --sider-padding: 1.5rem;
  }

  aside {
    height: var(--sider-height); */
    /* width: 100%; */
    /* padding: var(--sider-padding); */
  /* }

  .fixed {
    height: 100vh;
    width: 20%;
    position: fixed;
  }

  .scroll > div {
    overflow-y: scroll;
    -webkit-overflow-scrolling: touch;
    margin-right: -999rem;
    padding-right: 999rem;
    width: 100%;
  } */
</style>

<aside class:scroll>
  <div class:fixed>
    <slot />
  </div>
</aside>
