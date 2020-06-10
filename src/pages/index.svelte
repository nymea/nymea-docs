<script>
  import Col from '../_components/grid/Col.svelte';
  import Grid from '../_components/grid/Grid.svelte';
  import Row from '../_components/grid/Row.svelte';
  import Button from '../_components/base/Button.svelte';
  import Logo from '../_components/Logo.svelte';
</script>

<style>
  section {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-09) + var(--space-07)) 0 var(--space-10);
  }

  section:first-child {
    border-top: 0;
  }

  @media only screen and (min-width: 64em) {
    section {
      padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    }
  }

  #introduction {
    background-color: var(--silver-base);
  }

  #introduction header h1 {
    color: var(--grey-base);
    font-size: 1.875rem;
    font-weight: 400;
    /* letter-spacing: -0.025em; */
    line-height: 3rem;
    margin-bottom: var(--space-04);
  }

  #introduction header p {
    font-weight: 500;
    font-size: 3rem;
    line-height: 3rem;
    margin-bottom: var(--space-09);
    overflow: hidden;
  }

  #introduction header > :global(a) {
    margin: 1.5rem 0 1rem;
  }

  @media only screen and (min-width: 64em) {
    #introduction header h1 {
      font-size: 2.25rem;
      line-height: 3rem;
    }

    #introduction header p {
      font-size: 4.5rem;
      line-height: 4.5rem;
      /* margin-bottom: var(--space-04); */
    }
  }

  #for-whom {
    margin-top: 0;
  }

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

  section h2,
  section h3 {
    margin-bottom: var(--space-07);
  }

  #why ion-icon {
    color: var(--grey-base);
    height: var(--space-09);
    margin-top: var(--space-09);
    width: var(--space-09);
  }
</style>

<section id="introduction">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row middle>
      <Col span={{'xs': 10, 'md': 12}}>
        <header>
          <h1>nymea</h1>
          <!-- <Logo height="2rem" text="true" /> -->
          <p>The Open IoT Stack</p>
        </header>
        <Button text="Get started" link="documentation/overview/about-nymea">
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
          <p>When you're building your own IoT device, nymea will help with all the software efforts. Whether it's connecting your device to others, adding easy set-up features, creating smart hubs for all your devices or adding control and setup frontends, nymea's got your back.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="box">
          <header>
            <ion-icon name="rocket"></ion-icon>
            <h3>For Businesses</h3>
            <p>Build</p>
          </header>
          <p>Building IoT enabled customer grade products can be hard. We've ramped up with all the required know-how and with the nymea stack we'll be supporting your business. Whether it's fast prototyping and consulting, providing necessary components, building entire products or caring for deployments and updates.<!-- Together with our partners we offer in-field experience for all of those aspects. --></p>
        </div>
      </Col>
    </Row>
  </Grid>
</section>

<section id="why">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col center span={{'xs': 10, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 1, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
        <h2>Affair of the heart</h2>
        <p>We think that IoT devices, especially inside your home, do not have to be cloud connected all the time. Privacy and reliability are our main concerns. With that in mind we build everything with an offline-first approach. This results in blazing fast reaction times, full control over personal data and guarantees your product won't be rendered useless if the cloud provider you've been betting on shuts down their service.</p>
        <ion-icon name="heart"></ion-icon>
      </Col>
    </Row>
  </Grid>
</section>
