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
      <Col center>
        <h3>Nymea is a connection talent</h3>
      </Col>
    </Row>
    <Row>
      <Col middle center>
        <h4>Lights</h4>
      </Col>
      <Col middle center>
        <h4>Sensors</h4>
      </Col>
      <Col middle center>
        <h4>Access control</h4>
      </Col>
      <Col middle center>
        <h4>Weather</h4>
      </Col>
      <Col middle center>
        <h4>Energy meters</h4>
      </Col>
      <Col middle center>
        <h4>Media</h4>
      </Col>
      <Col middle center>
        <h4>Irrigation</h4>
      </Col>
      <Col middle center>
        <h4>Notifications</h4>
      </Col>
      <Col middle center>
        <h4>Presence awareness</h4>
      </Col>
      <Col middle center>
        <h4>And many more</h4>
      </Col>
    </Row>
    <Row>
      <Col>
        <img src="img/things/bulb-outline.svg" alt="Lights" />
      </Col>
      <Col center>
        <img src="img/things/thermometer-outline.svg" alt="Sensors" />
      </Col>
      <Col center>
        <img src="img/things/key-outline.svg" alt="Access control" />
      </Col>
      <Col center>
        <img src="img/things/partly-sunny-outline.svg" alt="Weather" />
      </Col>
      <Col center>
        <img src="img/things/speedometer-outline.svg" alt="Energy meters" />
      </Col>
      <Col center>
        <img src="img/things/volume-high-outline.svg" alt="Media" />
      </Col>
      <Col center>
        <img src="img/things/water-outline.svg" alt="Irrigation" />
      </Col>
      <Col center>
        <img src="img/things/chatbox-ellipses-outline.svg" alt="Notifications" />
      </Col>
      <Col center>
        <img src="img/things/location-outline.svg" alt="Presence" />
      </Col>
      <Col center>
        <img src="img/things/more-outline.svg" alt="More" />
      </Col>
    </Row>
    <Row>
      <Col center>
        <p>Connecting things to your smart home is easy and quick. See the list of <a href="documentation/overview/integrations">integrations</a>.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col center middle>
        <h3>Hazzle-free setup</h3>
      </Col>
    </Row>
    <Row>
      <Col center middle>
        <img src="img/touch-screen-and-pi-love.png" alt="RPi support"/>
      </Col>
      <Col center middle>
        <img src="img/nymea-ubuntu.svg" alt="Linux support"/>
      </Col>
    </Row>
    <Row>
      <Col center middle>
        <p>Ready to go Raspberry Pi images</p>
      </Col>
      <Col center middle>
        <p>Prebuilt packages for Ubuntu and Debian GNU/Linux</p>
      </Col>
    </Row>
    <Row>
      <Col center middle>
        <img src="img/mobile-app.png" alt="Mobile app"/>
      </Col>
      <Col center middle>
        <img src="img/desktop-app.png" alt="Desktop app"/>
      </Col>
    </Row>
    <Row>
      <Col center middle>
        <p>Supports all mobile...</p>
      </Col>
      <Col center middle>
        <p>... and stationary devices.</p>
      </Col>
    </Row>
    <Row>
      <Col middle>
        <img src="img/badges/appstore.png" alt=""/>
      </Col>
      <Col middle>
        <img src="img/badges/playstore.png" alt=""/>
      </Col>
      <Col middle>
        <img src="img/badges/open-store.svg" alt=""/>
      </Col>
      <Col middle>
        <img src="img/badges/snap-store.png" alt=""/>
      </Col>
      <Col middle>
        <img src="img/badges/windows.svg" alt=""/>
      </Col>
      <Col middle>
        <img src="img/badges/macos.svg" alt=""/>
      </Col>
    </Row>
    <Row>
      <Col center>
        <p>Check out all the installation options in the <a href="documentation/users/installation/gettingstarted">installation documentation</a>.</p>
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
      <Col center>
        <h3>Advanced configuration</h3>
      </Col>
    </Row>
    <Row>
      <Col center>
        <img src="img/configuration.png" alt="Configuration"/>
        <p>TODO: Make this image a bit smaller</p>
      </Col>
    </Row>
    <Row>
      <Col>
        <p>Even without the need of a smart home, nymea offers comprehensive configuration capabilities for your hardware. Headless network setup as client or access point, setting up an MQTT broker, easy remote access, running a web server, or updating your system is all right there at your fingertips when nymea is installed.</p>
        <p>Link to feature list</p>
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
