<script>
  import { screens } from './_showcases.js';
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  .showcases {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
  }

  .showcase,
  .phone-frame {
    margin-bottom: var(--space-07);
  }

  .showcases:nth-child(2) .showcase {
    margin-bottom: var(--space-09);
  }

  .showcases:nth-child(2) .phone-frame {
    margin-bottom: 0;
  }

  .showcase h3 {
    margin-bottom: var(--space-07);
  }

  .showcase p {
    color: var(--grey-darken-10);
  }
</style>

<section class="showcases">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col middle span={{'xs': 8, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="showcase">
          <h3>Collecing sensor data</h3>
          <p>Connecting sensors to nymea allows for monitoring plants, energy consumption, air quality, weather data and many more. In combination with smart rules heating, irrigation, ventilation and such can be controlled magically.</p>
        </div>
      </Col>
      <Col span={{'xs': 4, 'sm': 3, 'md': 3, 'lg': 3, 'xl': 3}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <div class="phone-frame">
          <img src="/img/showcases/showcase-collecting-sensor-data.svg" alt="">
        </div>
      </Col>
    </Row>
    
    <Row>
      <Col span={{'xs': 4, 'sm': 3, 'md': 3, 'lg': 3, 'xl': 3}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="phone-frame">
          <img src="/img/showcases/showcase-media.svg" alt="">
        </div>
      </Col>
      <Col middle span={{'xs': 8, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <div class="showcase">
          <h3>Media, integrated</h3>
          <p>Nymea allows setting alarmy by playing back your favorite music, dim your light to fit in with movie time or even automatically change radio station if your disliked songs are detected.</p>
        </div>
      </Col>
    </Row>

    <Row>
      <Col middle span={{'xs': 8, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="showcase">
          <h3>It's magic!</h3>
          <p>Define smart behaviors for your environment. Using easy to setup rules allows to create all sorts of scenarios. Turning on your light when it gets dark outside and you're at home is just one example. Just a few clicks and your custom behavior is ready to go.</p>
        </div>
      </Col>
      <Col span={{'xs': 4, 'sm': 3, 'md': 3, 'lg': 3, 'xl': 3}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <div class="phone-frame">
          <img src="/img/showcases/showcase-it-is-magic.svg" alt="">
        </div>
      </Col>
    </Row>

    <Row>
      <Col span={{'xs': 4, 'sm': 3, 'md': 3, 'lg': 3, 'xl': 3}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="phone-frame">
          <img src="/img/showcases/showcase-configuration.svg" alt="">
        </div>
      </Col>
      <Col middle span={{'xs': 8, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <div class="showcase">
          <h3>Configuration</h3>
          <p>Even without the need of a smart home, nymea offers comprehensive configuration capabilities for your hardware. Headless network setup as client or access point, setting up an MQTT broker, easy remote access, running a web server, or updating your system is all right there at your fingertips when nymea is installed.</p>
        </div>
      </Col>
    </Row>
  </Grid>
</section>

<section class="showcases">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col center span={{'xs': 8, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 2, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}>
        <div class="showcase">
          <h3>For the more advanced</h3>
          <p>If simple smart rules aren't enough, nymea offers optional scripting support to create really advanced use cases. The possibilities are endless.</p>
        </div>
      </Col>
    </Row>
    <Row>
      <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <div class="phone-frame">
          <img src="/img/showcases/showcase-scripting.svg" alt="">
        </div>
      </Col>
    </Row>
  </Grid>
</section>
