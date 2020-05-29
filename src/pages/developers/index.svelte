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
          <h1>Build smart.</h1>
          <p>With nymea you can focus on the use case right away. The ground work is done.</p>
        </header>
        <Button text="Get started" link="documentation/developers">
          <ion-icon name="arrow-forward-outline" slot="end"></ion-icon>
        </Button>
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
      <Col middle>
        <h2>Easy, slick and flexible.</h2>
        <p>With nymea you pick what you need. Be it connecting things, APIs or frontends to your home-brew things. Be it writing low level device integrations or scripting fancy behaviors. Be it a full smart home solution or just setting up an MQTT broker that can send push notifications. You imagine it, nymea helps building it.</p>
      </Col>
      <Col>
        <img src="img/bricks.png" alt="Building blocks"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Tinkering made easy</h2>
        <p>For home brew IoT projects, nymea offers a comprehensive set of ready-made tools. There are tons of home brew tutorials out there that transform a Rasperry Pi into a purpose made IoT "thing". Instead of hand crafting that all from scratch every time, why not just install nymea and interact with your device from a remote JSON-RPC API instead of starting to type low level C code?<br>For many use cases coding isn't required at all as nymea handles a lot out of the box already.</p>
      </Col>
    </Row>
    <Row>  
      <Col>
      </Col>
      <Col>
        <img src="img/ADS1115.jpg" alt="I²C"/>
      </Col>
      <Col>
      </Col>
      <Col>
        <img src="img/one-wire-sensor.png" alt="One Wire"/>
      </Col>
      <Col>
      </Col>
      <Col>
        <img src="img/gpio.jpeg" alt="GPIO"/>
      </Col>
      <Col>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Low level when you need it, high level when you want it</h2>
        <p>While still being close enough to bare metal with C++/Qt in order to run fast and consume little resources, nymea abstracts all the really low level stuff away from the developer and provides an easy to use Object-Oriented API for IoT related APIs. Integrations and automation behaviors can be created using C++ for full power and flexibility, or JavaScript for the ease of use.</p>
      </Col>
    </Row>
    <Row>
      <Col>
        <img src="img/code-low.svg" alt="C++"/>
      </Col>
      <Col>
        <img src="img/code-high.svg" alt="C++"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Headless setups</h2>
        <p>When building any device, there's always the one question coming up. How would the user connect it to the network? nymeas network management APIs solve that issue by providing a Bluetooth-To-WiFi setup, ready to be installed on any Linux based device and with a client already deployed on app stores.</p>
      </Col>
      <Col>
        <img src="img/berrylan.gif" style="background: url(img/device-frame-iphone-6-8.svg) no-repeat top center; background-size:contain;" alt="Bt-Wireless setup"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Nymea is a communication talent</h2>
        <p>IoT often requires to interact with low level hardware like I2C, GPIO, One-Wire or connecting to networking protocols like COAP, ZigBee, Bluetooth and more. nymea believes that none of these should be reinvented all the time and abstracts the hard and boring bits like threading, parsing and memory management away from the developer allowing them to focusing on the actual use case.</p>
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
        <h2>Servers, intergrated</h2>
        <p>MQTT broker made easy. Take the nymea image, boot it up, and have your MQTT server running. With nymea:app it is ready to configure users and permissions.<br>
        Need an on-device webserver without wanting to edit config files? Just enable it in the nymea settings and be done with it.</p>
      </Col>
    </Row>
    <Row>
      <Col>
        <img src="img/mqtt-broker.png" alt="MQTT broker"/>
      </Col>
      <Col>
        <img src="img/webserver.png" alt="Web server"/>
      </Col>
    </Row>
  </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <h2>Need help?</h2>
      </Col>
    </Row>
    <Row>
      <Col>
      </Col>
      <Col center>
        <img src="img/community/discourse.svg" alt="Discourse"/>
        <p><a href="https://forum.nymea.io" target="_blank">Ask for help in our forum</a></p>
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
  </Grid>
</section>
