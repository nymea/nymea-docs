<script>
  import Col from '../../components/grid/Col.svelte';
  import Grid from '../../components/grid/Grid.svelte';
  import Row from '../../components/grid/Row.svelte';
</script>

<style>
  header p {
    font-size: 1.875rem;
    line-height: 3rem;
  }
</style>

<svelte:head>
	<title>businesses &middot; nymea</title>
</svelte:head>

<section>
  <Grid>
    <Row>
      <Col middle>
        <header>
          <h1>Be smart.</h1>
          <p>Build IoT business, not IoT devices.</p>
        </header>
        <a href="documentation/developers" class="button">Get started</a>
      </Col>
      <Col>
        <img src="img/smart-home.png" alt="Smart home"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col middle center>
        <h3>What we offer</h3>
        <p>Nymea GmbH is here to support development of your IoT product with our experience in all phases, from planning to rollout and maintenance. Together with our partners we offer experience in all those fields of the product lifecycle.</p>
            <p>&middot; Consulting on Hardware/Software evaluation.</p>
            <p>&middot; Adding individual features to your product, like easy setup, integrations to others, remote connection, Alexa/Google integration and many more.</p>
            <p>&middot; Building entire smart home gateways.</p>
            <p>&middot; Apps for nymea based IoT products with your company branding.</p>            
            <p>&middot; OTA upgrades.</p>
            <p>&middot; Industrial device monitoring.</p>
      </Col>
    </Row>
    <Row>
      <Col center>
        <h4><a href="">Let's build somthing great together! TODO: Link to contact form</a></h4>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <img src="img/nymea-integrations.png" alt="Integrations"/>
      </Col>
      <Col middle center>
        <h3>Save thousands of integration hours</h3>
        <p>Extend connectivity of your IoT device to virtually anything with nymea. Adding new integrations is easily done via over-the-air updates.</p>
      </Col>
    </Row>
  </Grid>
</section>


<section>
  <Grid>
    <Row>
      <Col middle center>
        <p>Nymea is ready to be integrated on a variety of GNU/Linux based devices. Be it Yocto, Ubuntu Core, Debian or anything else, we've got the experience in delivering the nymea stack to your platform of choice.</p>
      </Col>
      <Col>
        <img src="img/distributions.svg" alt="Distributions"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <img src="img/nymea_vs_java_footprint.png" alt="Footprint"/>
      </Col>
      <Col center middle>
        <h3>The worlds smallest footprint</h3>
        <p>A powerful, yet lean addon for your device firmware.</p>
        <p>nymea does not require a power horse, it's perfectly fine with low cost modules as long as GNU/Linux is available for them.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
    <Col center middle>
        <h3>Also need hardware?</h3>
        <p>Together with our partners we have developed embedded devices ready to base your IoT product on.</p>
      </Col>
       <Col>
        <img src="img/HW-SW-modules.png" alt="HW"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col center>
        <h3>Our partners</h3>
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
