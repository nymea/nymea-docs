<script>
  import Col from '../../components/grid/Col.svelte';
  import Grid from '../../components/grid/Grid.svelte';
  import Row from '../../components/grid/Row.svelte';
</script>

<style></style>

<svelte:head>
	<title>users &middot; nymea</title>
</svelte:head>

<section>
  <Grid>
    <Row>
      <Col middle>
        <h3>Nymea gets you up and running with your Smart Home setup in no time.</h3>
        <a href="documentation/users/installation/gettingstarted">Learn more</a>
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
      <Col>
        <img src="img/plugnplay.svg" alt="Plug'n Play">
      </Col>
      <Col middle>
        <h3>Easy to use, yet powerful</h3>
        <p>Nymea does not require editing cryptic configuration files, it can be configured and controlled entirely using your smart phone or PC.</p>
      </Col>
    </Row>
  </Grid>
</section>
        
<section>
  <Grid>
    <Row>
      <Col middle>
        <h3>Local-first approach</h3>
        <p>Nymea ensures that your data is kept where it belongs, locally in your home. Besides the privacy advantage, this also keeps users independent form cloud vendors, and doesn't require an always-on internet connection.</p>
      </Col>
      <Col>
        <img src="img/shield.svg" alt="Privacy focused">
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <img src="img/open-source.svg" alt="Open Source"/>
      </Col>
      <Col middle>
        <h3>Free and Open Source</h3>
        <p>Nymea is comitted to open source software. Anything we do can be inspected, tuned and shared by users.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <h2>Features</h2>
        <p>Nymea is a connection talent. Connecting things to your smart home is easy and quick.</p>
        <p>Advanced configuration. Even without the need of a smart home, nymea offers comprehensive configuration capabilities for your hardware. Headless network setup as client or access point, setting up an MQTT broker, easy remote access, running a web server, or updating your system is all right there at your fingertips when nymea is installed.</p>
        <p>Link to feature list</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <img src="img/magic.png" alt="It's magic"/>
      </Col>
      <Col middle>
        <h3>It's magic!</h3>
        <p>Define smart behaviors for your environment. Using easy to setup rules allows to create all sorts of scenarios. Turning on your light when it gets dark outside and you're at home is just one example. Just a few clicks and your custom behavior is ready to go.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col middle>
        <h3>For the more advanced</h3>
        <p>If simple smart rules aren't enough, nymea offers optional scripting support to create really advanced use cases. The possibilities are endless.</p>
      </Col>
      <Col>
        <img src="img/scripting.png" alt="Scripting support"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col>
        <h2>Showcases</h2>
        <p>nymea:app overview connected to a Raspberry Pi smart home setup</p>
        <p>nymea:app color light page</p>
        <p>nymea:app sensors graph page</p>
        <p>nymea:app settings page</p>
        <p>nymea on a touchscreen rpi</p>
        <p>nymea on a hot tub</p>
        <p>BerryLan</p>
      </Col>
    </Row>
  </Grid>
</section>
