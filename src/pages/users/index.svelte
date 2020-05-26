<script>
  import Col from '../../_components/grid/Col.svelte';
  import Grid from '../../_components/grid/Grid.svelte';
  import Row from '../../_components/grid/Row.svelte';
  import Button from '../../_components/base/Button.svelte';
</script>

<style>
  .box {
    margin-bottom: 3rem;
  }

  .box header {
    margin-bottom: 1.5rem;
  }

  .box header ion-icon {
    font-size: 1.875rem;
    /* letter-spacing: 0.01em; */
    line-height: 3rem;
    margin-bottom: 1.25rem;
  }

  .box header h3 {
    margin-bottom: 0.25rem;
  }

  .box header p {
    color: var(--turquoise-base);
    font-size: 0.8rem;
    text-transform: uppercase;
  }

  @media only screen and (min-width: 48em) {
    .box {
      margin-bottom: 0;
    }
  }

  .integration {
    color: var(--text-color);
    display: block;
    padding: 0.75rem;
    text-align: center;
    text-decoration: none;
  }

  .integration ion-icon {
    font-size: 2.25rem;
    line-height: 3rem;
    margin-bottom: 0.75rem;
  }

  .platforms {
    display: flex;
    margin-top: var(--space-07);
  }

  .platforms li {
    margin: 0;
  }

  .platforms ion-icon {
    font-size: 1.875rem;
    line-height: 3rem;
  }

  .step {
    margin-bottom: var(--space-09);
  }

  @media only screen and (min-width: 48em) {
    .step {
      margin-bottom: 0;
    }
  }

  section {
    border-bottom: 1px solid #efefef;
    padding: var(--space-09) 0 var(--space-10);
  }

  section h2,
  section h3 {
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

  #integrations {
    border-bottom: 1px solid #efefef;
  }

  #integrations :global(.row:nth-child(2)) {
    /* padding: 4.5rem 0; */
    padding: var(--space-07) 0;
    /* position: relative;
    z-index: 0; */
  }

  /* #integrations :global(.row:nth-child(2)::after) {
    background-color: red;
    content: "";
    height: var(--space-07);
    position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
    z-index: 1;
  } */

  #integrations :global(.row:nth-child(2) .col) {
    border-left: 1px solid #efefef;
    margin: 0;
    -webkit-overflow-scrolling: touch;
    position: relative;
  }

  #integrations :global(.row:nth-child(2) .col:first-child) {
    border-left: 0;
  }

  #integrations h6 {
    margin-top: auto;
  }

  #integrations a:hover ion-icon,
  #integrations a:hover h6 {
    transition: transform 0.1s ease-in-out;
  }

  #integrations a:hover ion-icon {
    transform: translateY(-0.375rem);
  }

  #integrations a:hover h6{
    transform: translateY(0.375rem);
  }

  #integrations :global(.col h6) {
    margin-bottom: 0;
  }
</style>

<section id="introduction">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col middle span={{'xs': 12, 'md': 8}} order={{'xs': 2, 'sm': 0}}>
        <header>
          <h1>Live smart.</h1>
          <p>Nymea gets you up and running with your Smart Home setup in no time.</p>
        </header>
        <Button text="Get started" link="documentation/users/installation/getting-started">
          <ion-icon name="arrow-forward-outline" slot="end"></ion-icon>
        </Button>
      </Col>
      <!-- <Col span={{'xs': 12, 'md': 6}} order={{'xs': 1, 'sm': 0}}>
        <img src="img/smart-home.png" alt="Smart home"/>
      </Col> -->
    </Row>
  </Grid>
</section>

<section id="features">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon name="body"></ion-icon>
            <h3>Easy but powerful</h3>
            <p>...</p>
          </header>
          <p>Nymea does not require editing cryptic configuration files, it can be configured and controlled entirely using your Smartphone or PC.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon name="shield-checkmark"></ion-icon>
            <h3>Local-first approach</h3>
            <p>...</p>
          </header>
          <p>Nymea ensures that your data is kept where it belongs, locally in your home. Besides the privacy advantage, this also keeps you independent from cloud vendors, and doesn't require an always-on internet connection.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon src="img/open-source-initiative.svg"></ion-icon>
            <h3>Free and Open Source</h3>
            <p>...</p>
          </header>
          <p>Nymea is comitted to open source software. Anything we do can be inspected, tuned and shared by our community.</p>
        </div>
      </Col>
    </Row>
  </Grid>
</section>

<section id="integrations">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'md': 8}}>
        <h2>Connection talent</h2>
        <p>Connecting things to your smart home is easy and quick. See the list of available <a href="documentation/overview/integrations">integrations</a>.</p>
      </Col>
    </Row>
    <Row wrap={false}>
      <Col>
        <a href="documentation/overview/integrations?category=light" class="integration">
          <ion-icon name="bulb"></ion-icon>
          <h6>Lights</h6>
        </a>
      </Col>
      <Col>
        <a href="documentation/overview/integrations?category=sensor" class="integration">
          <ion-icon name="thermometer"></ion-icon>
          <h6>Sensors</h6>
        </a>
      </Col>
      <Col>
        <a href="documentation/overview/integrations?category=lock" class="integration">
          <ion-icon name="key"></ion-icon>
          <h6>Access control</h6>
        </a>
      </Col>
    <!-- </Row>
    <Row> -->
      <Col>
        <a href="documentation/overview/integrations?category=weather" class="integration">
          <ion-icon name="partly-sunny"></ion-icon>
          <h6>Weather</h6>
        </a>
      </Col>
      <!-- <Col>
        <a href="." class="integration">
          <ion-icon name="speedometer"></ion-icon>
          <h6>Energy Meters</h6>
        </a>
      </Col> -->
      <Col>
        <a href="documentation/overview/integrations?category=multimedia" class="integration">
          <ion-icon name="play"></ion-icon>
          <h6>Media</h6>
        </a>
      </Col>
    <!-- </Row>
    <Row> -->
      <Col>
        <a href="documentation/overview/integrations?category=tool,sensor" class="integration">
          <ion-icon name="water"></ion-icon>
          <h6>Irrigation</h6>
        </a>
      </Col>
      <Col>
        <a href="documentation/overview/integrations?category=notification" class="integration">
          <ion-icon name="notifications"></ion-icon>
          <h6>Notifications</h6>
        </a>
      </Col>
      <Col>
        <a href="documentation/overview/integrations?category=online-service" class="integration">
          <ion-icon name="location"></ion-icon>
          <h6>Presence Awareness</h6>
        </a>
      </Col>
    <!-- </Row>
    <Row> -->
      <Col>
        <a href="documentation/overview/integrations" class="integration">
          <ion-icon name="ellipsis-horizontal"></ion-icon>
          <h6>Many More</h6>
        </a>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'md': 4}}>
        <div class="step">
          <h2>Install.</h2>
          <p>Nymea can be installed on various platforms. Download our prebuilt packages for Ubuntu or Debian GNU/Linux. You can also try one of our ready-to-go Raspberry Pi images.</p>
        
          <ul class="platforms">
            <li>
              <ion-icon src="img/ubuntu.svg"></ion-icon>
            </li>
            <li>
              <ion-icon src="img/debian.svg"></ion-icon>
            </li>
            <li>
              <ion-icon src="img/raspberry-pi.svg"></ion-icon>
            </li>
          </ul>
        </div>
      </Col>
      <Col span={{'xs': 12, 'md': 4}}>
        <div class="step">
          <h2>Setup.</h2>
          <p>Download our App to setup nymea. It is available for mobile and stationary devices on iOS, Android, Ubuntu Touch, MacOS, Windows and Linux Desktops.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'md': 4}}>
        <div class="step">
          <h2>Play.</h2>
          <p>Discover nymea. Connect things and let the magic happen. The possibilities are endless.</p>
        </div>
      </Col>
    </Row>
    <Row>
      <Col center>
        <p>Check out all the installation options in the <a href="documentation/users/installation/gettingstarted">installation documentation</a>.</p>
      </Col>
    </Row>
  </Grid>
</section>

<!-- <section>
  <Grid>
    <Row>
      <Col>
        <h2>Hazzle-free setup</h2>
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
</section> -->

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
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
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
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
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
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
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
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
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
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
