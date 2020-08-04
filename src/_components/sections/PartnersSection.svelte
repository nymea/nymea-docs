<script>
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  .partners {
    background: linear-gradient(135deg, var(--grey-darken-30), var(--grey-darken-40));
    border-bottom: 1px solid var(--grey-darken-40);
    border-top: 1px solid var(--grey-darken-40);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-09) + var(--space-07)) 0 var(--space-10);
  }

  @media only screen and (min-width: 64em) {
    .partners {
      padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    }
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
    margin-bottom: var(--space-07);
    margin-top: var(--space-07);
  }

  .partner {
    display: flex;
    height: 100%;
    justify-content: center;
    padding-top: var(--space-07);
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
        <a href="https://www.marantec-group.com/" target="_blank" rel="noopener" class="partner">
          <img src="/img/partners/marantec-group.svg" alt="marantec group" />
        </a>
      </Col>
      <Col>
        <a href="https://www.streamunlimited.com/" target="_blank" rel="noopener" class="partner">
          <img src="/img/partners/stream-unlimited.svg" alt="Stream Unlimited" />
        </a>
      </Col>
      <Col>
        <a href="https://www.qt.io/" target="_blank" rel="noopener" class="partner">
          <img src="/img/partners/qt-company.svg" alt="The Qt Company" />
        </a>
      </Col>
      <Col>
        <a href="https://ubuntu.com/" target="_blank" rel="noopener" class="partner">
          <img src="/img/partners/ubuntu.svg" alt="ubuntu" />
        </a>
      </Col>
      <Col>
        <a href="https://www.dh-electronics.com/" target="_blank" rel="noopener" class="partner">
          <img src="/img/partners/dh-electronics.svg" alt="DH electronics" />
        </a>
      </Col>
      <Col>
        <a href="https://www.usedatatolead.com" target="_blank" rel="noopener" class="partner">
          <img src="/img/partners/UDTL_Logo.svg" alt="Use Data To Lead" />
        </a>
      </Col>
    </Row>
  </Grid>
</section>
