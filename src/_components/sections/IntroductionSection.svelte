<script>
  import Button from '../base/Button.svelte';
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';

  export let title = 'Title';
  export let subTitle = 'Subtitle';
  export let buttonIconName = 'arrow-forward';
  export let buttonIconSrc = '';
  export let buttonText = 'More';
  export let buttonLink = '#';
  export let showButton = true;
</script>

<style>
  .introduction {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    /* border-top: 1px solid var(--silver-darken-10); */
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-09)) 0;
  }

  .introduction header h1 {
    font-size: 3rem;
    line-height: 3rem;
    margin-bottom: var(--space-04);
  }

  .introduction header p {
    color: var(--grey-base);
    font-size: 1.25rem;
    line-height: 1.5rem;
    font-weight: 400;
    margin-bottom: var(--space-09);
  }

  @media only screen and (min-width: 64em) {
    .introduction header h1 {
      font-size: 4.5rem;
      line-height: 4.5rem;
      margin-bottom: var(--space-04);
    }

    .introduction header p {
      font-size: 2.25rem;
      line-height: 3rem;
    }
  }
</style>

<section class="introduction">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col middle span={{'xs': 8, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} order={{'xs': 2, 'sm': 0, 'md': 0, 'lg': 0, 'xl': 0}}>
        <header>
          <h1>{title}</h1>
          <p>{subTitle}</p>
        </header>

        {#if showButton === true}
          {#if buttonIconName}
            <Button text={buttonText} link={buttonLink}>
              <ion-icon name={buttonIconName} slot="end"></ion-icon>
            </Button>
          {:else if buttonIconSrc}
            <Button text={buttonText} link={buttonLink}>
              <ion-icon src={buttonIconSrc} slot="end"></ion-icon>
            </Button>
          {:else}
            <Button text={buttonText} link={buttonLink}></Button>
          {/if}
        {/if}
      </Col>
    </Row>
  </Grid>
</section>
