<script>
  import Col from '../../components/grid/Col.svelte';
  import Grid from '../../components/grid/Grid.svelte';
  import Row from '../../components/grid/Row.svelte';
</script>

<style></style>

<svelte:head>
	<title>developers &middot; nymea</title>
</svelte:head>

<section>
  <Grid>
    <Row>
      <Col>
        <h1>Developers</h1>
        <p>Nymea gets you up and running with your Smart Home setup in no time.</p>
        <a href="documentation/developers">Learn more</a>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <h2>Mission</h2>
        <p>Easy, slick and flexible.</p>
        <p>While still being close enough to bare metal with C++/Qt in order to run fast and consume little resources, nymea abstracts all the really low level stuff away from the developer and provides an easy to use Object-Oriented API for IoT related APIs.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <h2>Features</h2>
        <p>Home-Brew IoT projects. For tinkers, nymea offers a comprehensive set of ready-made tools. There are tons of home brew tutorials out there that transform a Rasperry Pi into a purpose made IoT "thing". Instead of hand crafting that all from scratch every time, with nymea efforts are minimized and features like remote APIs, client apps and configuration tools are available just like that.</p>
        <p>When building any device, there's always the one question coming up. How would the user connect it to the network? nymeas networkmanagement APIs solve that issue by providing a Bluetooth-To-WiFi setup, ready to be installed on any Linux based device and with a client already deployed on app stores.</p>
        <p>MQTT broker made easy. Take the nymea image, boot it up, and have your MQTT server running. With nymea:app ready to configure users and permissions.</p>
        <p>IoT often requires to interact with low level hardware like I2C, GPIO, One-Wire or connecting to networking protocols like COAP, ZigBee, Bluetooth and more. nymea believes that none of these should require error prone C code and abstracts the hard and boring bits like threading, parsing and memory management away from the developer to allow focusing on the actual use case.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <h2>Showcases</h2>
        <p>BerryLan</p>
        <p>Home-Brew sensor station</p>
      </Col>
    </Row>
  </Grid>
</section>
