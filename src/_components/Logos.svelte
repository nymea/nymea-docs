<script>
  import Col from './grid/Col.svelte';
  import Grid from './grid/Grid.svelte';
  import Row from './grid/Row.svelte';

  export let title = '';
  export let logos = [];
</script>

<style>
  h2,
  p {
    color: var(--silver-darken-20);
    color: var(--grey-base);
    /* color: var(--silver-transparent-base); */
  }

  h2 {
    margin-bottom: var(--space-09);
  }

  /* .logos {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
  } */

  /* .logo {
    text-align: center;
  } */

  .logos :global(.row:nth-child(2) .col) {
    margin-top: var(--space-07);
  }

  /* .logo ion-icon { */
  .logos :global(.row:nth-child(2) .col ion-icon) {
    /* color: var(--text-color);
    color: var(--silver-base); */
    color: var(--silver-darken-20);
    color: var(--grey-base);
    /* color: var(--silver-transparent-base); */
    height: var(--space-09);
    width: var(--space-09);
  }

  /* :global(.row:nth-child(2) .col ion-icon svg) {
    fill: var(--grey-base);
  } */
</style>

<Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
  <div class="logos">
    <Row>
      <Col center>
        <h2>{title}</h2>
      </Col>
    </Row>
    <Row>
      {#each logos as logo}
        <Col center>
          {#if logo.url}
            <a href={logo.url} alt={logo.title} title={logo.title} target="_blank">
              {#if logo.iconSrc}
                <ion-icon src={logo.iconSrc}></ion-icon>
              {:else if logo.iconName}
                <ion-icon name={logo.iconName}></ion-icon>
              {/if}
            </a>
          {:else}
            {#if logo.iconSrc}
              <ion-icon src={logo.iconSrc}></ion-icon>
            {:else if logo.iconName}
              <ion-icon name={logo.iconName}></ion-icon>
            {/if}
          {/if}
          {#if logo.title}
            <p>{logo.title}</p>
          {/if}
        </Col>
      {/each}
    </Row>
  </div>
</Grid>
<!-- <h2>{title}</h2>
<ul class="logos">
  {#each logos as logo}
    <li class="logo">
      {#if logo.url}
        <a href={logo.url} alt={logo.title} title={logo.title}>
          {#if logo.iconSrc}
            <ion-icon src={logo.iconSrc}></ion-icon>
          {:else if logo.iconName}
            <ion-icon name={logo.iconName}></ion-icon>
          {/if}
        </a>
      {:else}
        {#if logo.iconSrc}
          <ion-icon src={logo.iconSrc}></ion-icon>
        {:else if logo.iconName}
          <ion-icon name={logo.iconName}></ion-icon>
        {/if}
      {/if}
      {#if logo.title}
        <p>{logo.title}</p>
      {/if}
    </li>
  {/each}
</ul> -->
