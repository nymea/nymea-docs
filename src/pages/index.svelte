<script>
  import Col from '../_components/grid/Col.svelte';
  import Grid from '../_components/grid/Grid.svelte';
  import Row from '../_components/grid/Row.svelte';
  import Button from '../_components/base/Button.svelte';
</script>

<style>
  #introduction header p {
    margin-bottom: var(--space-09);
  }

  /* .box {
    padding: 0.75rem;
    position: relative;
  } */

  /* #for-whom :global(.col:first-of-type .box::after) {
    display: none;
  }

  .box::after {
    background-color: #efefef;
    content: "";
    position: absolute;
      bottom: 0;
      left: calc(var(--row-gap) / 2 * -1);
      top: 0;
    width: 1px;
  } */

  .box {
    margin-bottom: 3rem;
  }

  .box header {
    margin-bottom: 1.5rem;
  }

  .box header ion-icon {
    font-size: 1.875rem;
    letter-spacing: 0.01em;
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

  .carousel {
    
  }

  .carousel ul {
    display: flex;
    list-style-type: none;
    /* overflow-x: auto; */
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    -webkit-overflow-scrolling: touch;
  }

  .carousel p,
  .carousel li {
    
  }

  .carousel p {
    
  }

  .carousel li {
    border: 1px solid var(--silver-darken-20);
    flex: 0 0 25%;
    height: 4.5rem;
    justify-content: center;
    margin: 0;
    text-align: center;
  }

  section {
    border-bottom: 1px solid #efefef;
    padding: var(--space-09) 0 var(--space-10);
  }

  section h2,
  section h3 {
    margin-bottom: var(--space-07);
  }

  #introduction h1 {
    color: var(--grey-base);
    font-size: 2.25rem;
    font-weight: 400;
    letter-spacing: -0.025em;
    line-height: 5rem;
  }

  #introduction p {
    font-size: 4.5rem;
    font-weight: 500;
    line-height: 5rem;
    overflow: hidden;
  }

  #what-2 h6 {
    color: var(--grey-base);
    font-weight: 700;
    margin-bottom: 0;
    overflow: hidden;
    /* position: relative; */
    text-align: center;
    z-index: 1;
  }

  #what-2 h6::before,
  #what-2 h6::after {
    background-color: var(--silver-darken-20);
    content: "";
    display: inline-block;
    height: 1px;
    /* position: absolute; */
    position: relative;
    /* vertical-align: middle; */
    bottom: 0.375rem;
    width: 50%;
  }

  #what-2 h6::before {
    right: 0.5em;
    margin-left: -50%;
  }

  #what-2 h6::after {
    left: 0.5em;
    margin-right: -50%;
  }

  #what-2 h6 + div {
    /* background-color: var(--silver-darken-10); */
  }

  /* #introduction,
  #for-whom {
    margin-top: -9rem;
  }

  #introduction {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 6rem - 1.5rem);
    justify-content: center;
    margin-bottom: 3rem;
  }

  #introduction header h1 {
    color: #676767;
    font-size: 3rem;
    font-weight: 400;
    line-height: 3rem;
  }

  #introduction header p {
    color: #202020;
    font-size: 6rem;
    font-weight: 500;
    line-height: 7rem;
    margin: 0;
  }

  #for-whom .box {
    background-color: #fafafa;
    border-radius: 5px;
    height: 100%;
    padding: 3rem;
  }

  #for-whom header ion-icon {
    font-size: 2rem;
    line-height: 3rem;
    margin-bottom: 1.5rem;
  }

  #for-whom header h3 {
    margin-bottom: 0;
  }

  #for-whom header p {
    color: rgba(159, 200, 164, 1);
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.01em;
    line-height: 1.5rem;
    margin: 0 0 1.5rem;
    text-transform: uppercase;
  } */
</style>

<section id="introduction">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row middle>
      <Col span={{'xs': 10, 'md': 12}}>
        <header>
          <h1>nymea</h1>
          <p>The Open IoT Stack</p>
        </header>
        <Button text="Get started" link="documentation/overview">
          <ion-icon name="arrow-forward-outline" slot="end"></ion-icon>
        </Button>
      </Col>
    </Row>
  </Grid>
</section>

<section id="for-whom">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon name="people"></ion-icon>
            <h3>For Users</h3>
            <p>Play</p>
          </header>
          <p>nymea gets you up and running with your smart home setup in no time. Just install nymea:core and nymea:app and you're all set with a powerful smart home solution that does not require powerful hardware or fiddling with cryptic configuration files. Using 100% free and open source software.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon name="code-slash"></ion-icon>
            <h3>For Developers</h3>
            <p>Create</p>
          </header>
          <p>When you're building your own IoT device, nymea will help with all the software efforts. Whether it's connecting your device to others, adding easy set-up features, creating smart hubs for for all your devices or adding control and setup frontends, nymea's got your back.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon name="rocket"></ion-icon>
            <h3>For Businesses</h3>
            <p>Build</p>
          </header>
          <p>Building IoT enabled customer grade products can be hard. We've ramped up with all the required know-how and with the nymea stack we'll be supporting your business. Whether it's fast prototyping and consulting, providing needed components, building entire products or caring for deployments and updates.<!-- Together with our partners we offer in-field experience for all of those aspects. --></p>
        </div>
      </Col>
    </Row>
  </Grid>
</section>

<section id="what-2" class="viewsection">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 8}}>
        <h2>Built for connected devices</h2>
        <p>Connect lighting, media, heating, irrigations and sprinklers, garage doors, alarm systems and many more to a centralized, local and privacy focused control center with nymea. Or build your device running nymea to connect and integrate with other solutions, such as Alexa or Google Home.</p>
      </Col>
      <!-- <Col>
        <img src="img/nymea-integrations.png">
      </Col> -->
    </Row>
    <Row>
      <Col>
        <h6>Edge</h6>
        <div class="carousel">
          <p>Protocols</p>
          <ul>
            <li>Wi-Fi</li>
            <li>LoRa</li>
            <li>Z-Wave</li>
            <li>Bluetooth</li>
            <li>ZigBee</li>
          </ul>
        </div>
        <div class="carousel">
          <p>Bus Systems</p>
          <ul>
            <li>ModBus</li>
            <li>KNX</li>
            <li>Dali</li>
            <li>OPC UA</li>
            <li>BACnet</li>
          </ul>
        </div>
        <div class="carousel">
          <p>Devices</p>
          <ul>
            <li>Philips Hue</li>
            <li>...</li>
          </ul>
        </div>

        <h6>Cloud</h6>
        <div class="carousel">
          <p>Platforms</p>
          <ul>
            <li>Amazon Alexa</li>
            <li>Google Assistant</li>
            <li>IFTTT</li>
            <li>SmartThings</li>
            <li>Tuya</li>
          </ul>
        </div>
      </Col>
    </Row>
  </Grid>
</section>



<section id="why">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 8}}>
        <h2>Affair of the heart</h2>
        <p>We think that IoT devices, especially inside your home do not have to be cloud connected all the time. Privacy and reliability are our main concerns. With that in mind we build anything we do with a offline-first approach. This results in blazing fast reaction times, full control over personal data and guarantees your product won't be rendered useless if the cloud provider you've been betting on shuts down their service.</p>
      </Col>
      <Col>
          <ion-icon name="heart"></ion-icon>
      </Col>
    </Row>
  </Grid>
</section>

<section id="showcases">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Showcases</h2>
      </Col>
    </Row>
  </Grid>
</section>
