<script>
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  .partners {
    /* background: linear-gradient(180deg, var(--white), var(--silver-base)); */
    background: linear-gradient(135deg, var(--grey-darken-30), var(--grey-darken-40));
    /* border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10); */
    border-bottom: 1px solid var(--grey-darken-40);
    border-top: 1px solid var(--grey-darken-40);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    /* padding: var(--space-07) 0; */
  }

  .partners :global(.row:nth-child(2)) {
    justify-content: center;
  }

  .partners :global(.row:nth-child(2) .col) {
    flex-basis: 25%;
    flex-grow: 0;
  }

  h2 {
  /* h6 { */
    color: var(--grey-base);
    margin-bottom: var(--space-09);
    margin-top: var(--space-07);
  }

  .partner {
    display: flex;
    height: 100%;
    justify-content: center;
  }

  @media only screen and (min-width: 30em)  {
    .partner {
      padding: var(--space-04);
    }
  }

  @media only screen and (min-width: 48em)  {
    .partners :global(.row:nth-child(2) .col) {
      flex-basis: 15%;
    }

    .partner {
      padding: var(--space-07);
    }
  }
</style>


<section class="partners">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col center>
        <h2>Our partners</h2>
        <!-- <h6>Our partners</h6> -->
      </Col>
    </Row>
    <Row wrap>
      <Col>
        <a href="https://www.marantec-group.com/" class="partner">
          <img src="/img/partners/marantec-group.svg" alt="marantec group" />
        </a>
      </Col>
      <Col>
        <a href="https://www.streamunlimited.com/" class="partner">
          <img src="/img/partners/stream-unlimited.svg" alt="Stream Unlimited" />
        </a>
      </Col>
      <Col>
        <a href="https://www.qt.io/" class="partner">
          <img src="/img/partners/qt-company.svg" alt="The Qt Company" />
        </a>
      </Col>
      <Col>
        <a href="https://ubuntu.com/" class="partner">
          <img src="/img/partners/ubuntu.svg" alt="ubuntu" />
        </a>
      </Col>
      <Col>
        <a href="https://www.dh-electronics.com/" class="partner">
          <img src="/img/partners/dh-electronics.svg" alt="DH electronics" />
        </a>
      </Col>
    </Row>
  </Grid>
</section>