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
      <Col middle center>
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
      <Col middle center>
        <h3>Easy to use, yet powerful</h3>
        <p>Nymea does not require editing cryptic configuration files, it can be configured and controlled entirely using your smart phone or PC.</p>
      </Col>
    </Row>
  </Grid>
</section>
        
<section>
  <Grid>
    <Row>
      <Col middle center>
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
      <Col middle center>
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
      <Col middle center>
        <h3>It's magic!</h3>
        <p>Define smart behaviors for your environment. Using easy to setup rules allows to create all sorts of scenarios. Turning on your light when it gets dark outside and you're at home is just one example. Just a few clicks and your custom behavior is ready to go.</p>
      </Col>
    </Row>
    <Row>
      <Col middle center>
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
        <img src="img/sensors.png" alt="Sensors"/>
      </Col>
      <Col center middle>
        <h3>Collecing sensor data</h3>
        <p>Connecting sensors to nymea allows for monitoring plants, energy consumption, air quality, weather data and many more. In combination with smart rules heating, irrigation, ventilation and such can be controlled magically.</p>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
      <Col center middle>
        <h3>Media, integrated</h3>
        <p>Media playback and browsing integrated. Setting alarms with music playback, automatic ambiance lighting for movie time...</p>
      </Col>
    <Row>
      <Col>
        <img src="img/media-playback.png" alt="Media playback"/>
      </Col>
      <Col>
        <img src="img/media-browser.png" alt="Media browser"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid>
    <Row>
      <Col center>
        <h3>Join our community</h3>
      </Col>
    </Row>
    <Row>
      <Col>
      </Col>
      <Col center>
        <img src="img/community/discourse.svg" alt="Discourse"/>
        <p><a href="https://forum.nymea.io" target="_blank">Discuss in our forum</a></p>
      </Col>
      <Col>
      </Col>
      <Col center>
        <img src="img/community/telegram.svg" alt="Telegram"/>
        <p><a href="http://t.me/nymeacommunity" target="_blank">Chat with us on Telegram</a></p>
      </Col>
      <Col>
      </Col>
      <Col center>
        <img src="img/community/github.svg" alt="Github"/>
        <p><a href="https://github.com/nymea" target="_blank">Report bugs or fork the code on github</a></p>
      </Col>
      <Col>
      </Col>
    </Row>
    <Row>
      <Col center>
        <img src="img/community/twitter.svg" alt="Twitter"/>
        <p><a class="twitter-share-button" href="https://twitter.com/intent/tweet?text=&hashtags=nymea,IoT,smarthome" data-size="large" target="_blank">Tweet about nymea</a></p>
      </Col>
      <Col>
      </Col>
      <Col center>
        <img src="img/community/facebook.svg" alt="Facebook"/>
        <div id="fb-root"></div>
        <script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v7.0"></script>
        <div class="fb-like" data-href="https://nymea.io" data-width="" data-layout="button" data-action="like" data-size="small" data-share="true"></div>
      </Col>
      <Col>
      </Col>
      <Col center>
        <img src="img/community/diaspora.svg" alt="Diaspora"/>
        <a href="https://share.diasporafoundation.org/?title=diaspora* Advanced Sharer&url=https://nymea.io" rel="nofollow" target="_blank" style="padding: 3px 4px 2px; background: #fafafa; border: 1px solid #ddd; font-size: 13px; color: #222; text-decoration: none;">Share on diaspora*</a>
      </Col>
      <Col>
      </Col>
      <Col center>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" class="_1O4jTk-dZ-VIxsCuYB6OR8"><g><circle fill="#FF4500" cx="10" cy="10" r="10"></circle><path fill="#FFF" d="M16.67,10A1.46,1.46,0,0,0,14.2,9a7.12,7.12,0,0,0-3.85-1.23L11,4.65,13.14,5.1a1,1,0,1,0,.13-0.61L10.82,4a0.31,0.31,0,0,0-.37.24L9.71,7.71a7.14,7.14,0,0,0-3.9,1.23A1.46,1.46,0,1,0,4.2,11.33a2.87,2.87,0,0,0,0,.44c0,2.24,2.61,4.06,5.83,4.06s5.83-1.82,5.83-4.06a2.87,2.87,0,0,0,0-.44A1.46,1.46,0,0,0,16.67,10Zm-10,1a1,1,0,1,1,1,1A1,1,0,0,1,6.67,11Zm5.81,2.75a3.84,3.84,0,0,1-2.47.77,3.84,3.84,0,0,1-2.47-.77,0.27,0.27,0,0,1,.38-0.38A3.27,3.27,0,0,0,10,14a3.28,3.28,0,0,0,2.09-.61A0.27,0.27,0,1,1,12.48,13.79Zm-0.18-1.71a1,1,0,1,1,1-1A1,1,0,0,1,12.29,12.08Z"></path></g></svg>
        <a href="http://www.reddit.com/submit?url=https://nymea.io&title=Smart home with nymea">Share on reddit</a>
      </Col>
    </Row>
  </Grid>
</section>
