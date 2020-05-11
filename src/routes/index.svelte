<script>
  import Col from '../components/grid/Col.svelte';
  import Grid from '../components/grid/Grid.svelte';
  import MainPage from '../components/pages/MainPage.svelte';
  import Row from '../components/grid/Row.svelte';
</script>

<style>
  #introduction,
  #for-whom {
    margin-top: -9rem;
  }

  #introduction {
    display: flex;
    flex-direction: column;
    height: calc(100vh - 6rem - 1.5rem);
    justify-content: center;
    margin-bottom: 3rem;
    /* height: calc(100vh - 4.5rem); */
  }

  #introduction header {
    /* height: 10.5rem; */
    /* margin: 3rem 0; */
  }

  #introduction header h1 {
    color: #676767;
    font-size: 3rem;
    font-weight: 400;
    line-height: 3rem;
    /* margin-top: 13.5rem; */
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
    /* box-shadow: 0 1px 2px rgba(0,0,0,0.07), 
                0 2px 4px rgba(0,0,0,0.07), 
                0 4px 8px rgba(0,0,0,0.07), 
                0 16px 24px rgba(0,0,0,0.07); */
    /* color: #fafafa; */
    height: 100%;
    padding: 3rem;
  }

  #for-whom header {
    /* position: relative; */
  }

  #for-whom header ion-icon {
    /* color: rgba(0, 0, 0, 0.2); */
    font-size: 2rem;
    line-height: 3rem;
    margin-bottom: 1.5rem;
    /* position: absolute;
      right: 0;
      top: 0; */
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
  }
</style>

<svelte:head>
  <title>nymea</title>
</svelte:head>

<MainPage>
  <section id="introduction">
    <Grid>
      <Row middle>
        <Col>
          <header>
            <h1>nymea</h1>
            <p>The Open Iot Stack</p>
          </header>
        </Col>
      </Row>
    </Grid>
  </section>

  <section id="for-whom">
    <Grid>
      <Row>
        <Col>
          <div class="box">
            <header>
              <ion-icon name="people-outline"></ion-icon>
              <h3>For Users</h3>
              <p>Play</p>
            </header>
            <p>Nymea gets you up and running with your smart home setup in no time. Just install nymea core and nymea:app and you're all set with a powerful smart home solution that does not require powerful hardware or fiddling with cryptic configuration files. Using 100% free and open source software.</p>
          </div>
        </Col>
        <Col>
          <div class="box">
            <header>
              <ion-icon name="code-slash-outline"></ion-icon>
              <h3>For Developers</h3>
              <p>Create</p>
            </header>
            <p>When you're building your own IoT device, nymea will help with all the software efforts. Whether it's connecting your device to others, adding easy set-up features, creating smart hubs for for all your devices or adding control and setup frontends, nymea's got your back.</p>
          </div>
        </Col>
        <Col>
          <div class="box">
            <header>
              <ion-icon name="rocket-outline"></ion-icon>
              <h3>For Businesses</h3>
              <p>Build</p>
            </header>
            <p>Building IoT enabled customer grade products can be hard. We've ramped up with all the required know-how and with the nymea stack we'll be supporting your business. Whether it's fast prototyping and consulting, providing needed components, building entire products or caring for deployments and updates. Together with our partners we offer in-field experience for all of those aspects.</p>
          </div>
        </Col>
      </Row>
    </Grid>
  </section>
</MainPage>
