<script>
  import Logo from '../Logo.svelte';
</script>

<style>
  :root {
    --footer-background-color: #fafafa;
    --footer-height: 6rem;
    --footer-padding: 0;
  }

  footer {
    /* background-color: var(--footer-background-color); */
    border-top: 1px solid rgba(0, 0, 0, 0.1);
    height: var(--footer-height);
  }

  /* :root {
    --footer-background-color: #fafafa; */
    /* --footer-height: 4.5rem; */
    /* --footer-padding: 1.5rem;
  }

  footer { */
    /* background-color: var(--footer-background-color); */
    /* height: var(--footer-height); */
    /* padding: var(--footer-padding); */
    /* margin: 6rem 0 0; */
    /* padding: 0 0 1.5rem;

  }

  footer > div { */
    /* background-color: var(--footer-background-color); */
    /* border-radius: 3px; */
    /* margin-bottom: 1.5rem;
  }

  footer :global(.logo) {
    margin: 0 auto;
  }

  @media only screen and (min-width: 48em) {
    footer {
      padding: 0 6rem 1.5rem;
    }
  }

  @media only screen and (min-width: 64em) {

  }

  @media only screen and (min-width: 75em) {

  }

  @media only screen and (min-width: 105em) {

  } */
</style>

<footer>
  <!-- <div> -->
    <slot />
  <!-- </div>
  <Logo height="3rem" /> -->
</footer>
