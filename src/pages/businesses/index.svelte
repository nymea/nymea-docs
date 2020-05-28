<script>
  import Col from '../../_components/grid/Col.svelte';
  import Grid from '../../_components/grid/Grid.svelte';
  import Row from '../../_components/grid/Row.svelte';
  import Button from '../../_components/base/Button.svelte';
</script>

<style>
  section {
    border-bottom: 1px solid #efefef;
    padding: var(--space-10) 0;
  }

  section h2 {
    margin-bottom: var(--space-07);
  }

  header h1 {
    font-size: 4rem;
    line-height: 4.5rem;
    margin-bottom: var(--space-04);
  }

  header p {
    color: var(--grey-base);
    font-size: 1.25rem;
    line-height: 1.5rem;
    margin-bottom: var(--space-09);
  }

  @media only screen and (min-width: 48em) {
    header h1 {
      font-size: 4.5rem;
      line-height: 6rem;
    }

    header p {
      font-size: 1.5rem;
      line-height: 2rem;
    }
  }

  #introduction {
    background-color: var(--silver-base);
  }
</style>

<section id="introduction">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col middle span={{'xs': 12, 'md': 8}}>
        <header>
          <h1>Be smart.</h1>
          <p>Build IoT business, not IoT devices.</p>
        </header>
        <!-- <Button text="Get started" link="documentation/businesses">
          <ion-icon name="arrow-forward-outline" slot="end"></ion-icon>
        </Button> -->
      </Col>
      <!-- <Col>
        <img src="img/smart-home.png" alt="Smart home"/>
      </Col> -->
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>What we offer</h2>
        <p>Nymea GmbH is here to support development of your IoT product with our experience in all phases, from planning to rollout and maintenance. Together with our partners we offer experience in all those fields of the product lifecycle.</p>
        <ul>
          <li>Consulting on Hardware/Software evaluation.</li>
          <li>Adding individual features to your product, like easy setup, integrations to others, remote connection, Alexa/Google integration and many more.</li>
          <li>Building entire smart home gateways.</li>
          <li>Apps for nymea based IoT products with your company branding.</li>
          <li>OTA (Over The Air) Update.</li>
          <li>Industrial device monitoring.</li>
        </ul>
      </Col>
    </Row>
    <Row>
      <Col>
        <a href="">Let's build somthing great together! TODO: Link to contact form</a>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Save thousands of integration hours</h2>
        <p>Extend connectivity of your IoT device to virtually anything with nymea. Adding new integrations is easily done via over-the-air updates.</p>
      </Col>
      <Col>
        <img src="img/nymea-integrations.png" alt="Integrations"/>
      </Col>
    </Row>
  </Grid>
</section>


<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <p>Nymea is ready to be integrated on a variety of GNU/Linux based devices. Be it Yocto, Ubuntu Core, Debian or anything else, we've got the experience in delivering the nymea stack to your platform of choice.</p>
      </Col>
      <Col>
        <img src="img/distributions.svg" alt="Distributions"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>The worlds smallest footprint</h2>
        <p>A powerful, yet lean addon for your device firmware.</p>
        <p>nymea does not require a power horse, it's perfectly fine with low cost modules as long as GNU/Linux is available for them.</p>
      </Col>
      <Col>
        <img src="img/nymea_vs_java_footprint.png" alt="Footprint"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Also need hardware?</h2>
        <p>Together with our partners we have developed embedded devices ready to base your IoT product on.</p>
      </Col>
      <Col>
        <img src="img/HW-SW-modules.png" alt="HW"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col center>
        <h2>Our partners</h2>
      </Col>
    </Row>
    <Row>
      <Col middle>
        <img src="img/partners/marantec.png" alt="Marantec">
      </Col>
      <Col middle>
        <img src="img/partners/streamunlimited.png" alt="StreamUnlimited">
      </Col>
      <Col middle>
        <img src="img/partners/TheQtCompany_Logo.png" alt="The Qt Company">
      </Col>
      <Col middle>
        <img src="img/partners/ubuntu.svg" alt="Ubuntu">
      </Col>
      <Col middle>
        <img src="img/partners/dh_electronics.svg" alt="DH Electronics">
      </Col>
    </Row>
  </Grid>
</section>
