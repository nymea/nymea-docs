<script>
  import { url } from '@sveltech/routify';
  import Col from '../_components/grid/Col.svelte';
  import Row from '../_components/grid/Row.svelte';
  import IntroductionSection from '../_components/sections/IntroductionSection.svelte';
  import LogosSection from '../_components/sections/LogosSection.svelte';
  import Section from '../_components/sections/Section.svelte';
</script>

<style>
  h2 {
    margin-bottom: var(--space-07);
  }
</style>

<IntroductionSection
  title="Create smart."
  subTitle="With nymea you can focus on your use case. The ground work is done."
  buttonText="Get started"
  buttonLink={$url('/documentation/developers')} />

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Easy, slick and flexible.</h2>
      <p>With nymea you pick what you need. Be it connecting things, APIs or frontends to your home-brew things. Be it writing low level device integrations or scripting fancy behaviors. Be it a full smart home solution or just setting up an MQTT broker that can send push notifications. You imagine it, nymea helps building it.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Tinkering made easy</h2>
      <p>For home brew IoT projects, nymea offers a comprehensive set of ready-made tools. There are tons of home brew tutorials out there that transform a Rasperry Pi into a purpose made IoT "thing". Instead of hand crafting that all from scratch every time, why not just install nymea and interact with your device from a remote JSON-RPC API instead of starting to type low level C code?</p>
      <p>For many use cases coding isn't required at all as nymea handles a lot out of the box already.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Low level when you need it, high level when you want it</h2>
      <p>While still being close enough to bare metal with C++/Qt in order to run fast and consume little resources, nymea abstracts all the really low level stuff away from the developer and provides an easy to use Object-Oriented API for IoT related APIs. Integrations and automation behaviors can be created using C++ for full power and flexibility, or JavaScript for the ease of use.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Headless setup</h2>
      <p>When building any device, there's always the one question coming up. How would the user connect it to the network? nymeas network management APIs solve that issue by providing a Bluetooth-To-WiFi setup, ready to be installed on any Linux based device and with a client already deployed on app stores.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Nymea is a communication talent</h2>
      <p>IoT often requires to interact with low level hardware like I2C, GPIO, One-Wire or connecting to networking protocols like COAP, ZigBee, Bluetooth and more. nymea believes that none of these should be reinvented all the time and abstracts the hard and boring bits like threading, parsing and memory management away from the developer allowing them to focusing on the actual use case.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Servers, integrated</h2>
      <p>MQTT broker made easy. Take the nymea image, boot it up, and have your MQTT server running. With nymea:app it is ready to configure users and permissions. Need an on-device webserver without wanting to edit config files? Just enable it in the nymea settings and be done with it.</p>
    </Col>
  </Row>
</Section>

<LogosSection />
