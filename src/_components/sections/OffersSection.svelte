<script>
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  .offers {
    /* background-color: var(--silver-base); */
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
  }

  h2 {
    margin-bottom: var(--space-07);
  }

  h2 + p {
    color: var(--grey-base);
    font-size: 1.125rem;
    margin-bottom: var(--space-07);
  }

  .offer {
    margin-top: var(--space-10);
    padding-right: var(--space-07);
  }

  .offer:firs-of-type {
    margin-top: 0;
  }

  .offer header {
    margin-bottom: var(--space-07);
  }

  .offer header ion-icon {
    /* color: var(--turquoise-darken-20); */
    color: var(--text-color);
    font-size: 1.875rem;
    line-height: 3rem;
    margin-bottom: 1.25rem;
  }

  .offer header h3 {
    margin-bottom: 0.25rem;
  }

  .offer header p {
    color: var(--turquoise-darken-20);
    /* color: var(--grey-base); */
    /* color: var(--text-color); */
    font-size: 0.8rem;
    letter-spacing: 0.01em;
    text-transform: uppercase;
  }

  .offer header + p {
    color: var(--grey-darken-10);
  }
</style>

<section class="offers">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <h2>What we offer</h2>
        <p>Nymea GmbH is here to support development of your IoT product with our experience in all phases, from planning to rollout and maintenance. Together with our partners we offer experience in all those fields of the product lifecycle.</p>
      </Col>
    </Row>
    <Row>
      <!-- <Col span={{'xs': 10, 'sm': 6, 'md': 6, 'lg': 6, 'xl': 6}} offset={{'xs': 2, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}} > -->
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="offer">
          <header>
            <ion-icon name="star"></ion-icon>
            <h3>Individual IoT Features</h3>
          </header>
          <p>Adding individual features to your product, like easy setup, platform integrations, 3rd party interoperability, remote connection, Alexa/Google integration and many more.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}>
        <div class="offer">
          <header>
            <ion-icon name="home"></ion-icon>
            <h3>Smart Home</h3>
          </header>
          <p>Embedding an entire smart home gateway into your product, including App, Smart Rules and integration with other IoT devices and services.</p>
        </div>
      </Col>
    </Row>
    <Row>
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="offer">
          <header>
            <ion-icon name="shield-checkmark"></ion-icon>
            <h3>Evaluation</h3>
          </header>
          <p>We help evaluating your IoT device plans. If unsure which radio technology, which hardware modules or cloud partners should be used, we provide guidance using our long term experience in the field.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}>
        <div class="offer">
          <header>
            <ion-icon name="logo-apple-appstore"></ion-icon>
            <h3>Apps</h3>
          </header>
          <p>Use our Frontend-Libraries to build Apps for all mobile and desktop platforms (and soon for the browser). Or use our prebuilt Smart Home App and customize it to your needs and branding guidelines.</p>
        </div>
      </Col>
    </Row>
    <Row>
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="offer">
          <header>
            <ion-icon name="sync"></ion-icon>
            <h3>Updates</h3>
          </header>
          <p>IoT devices need to be kept up to date. Nymea provides update services using various backends like Mender, SWUpdate, Ubuntu Core and more.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}>
        <div class="offer">
          <header>
            <ion-icon name="cloud"></ion-icon>
            <h3>Services</h3>
          </header>
          <p>Value adding services for your products.</p>
        </div>
      </Col>
    </Row>
  </Grid>
</section>
