<script>
  import Col from '../_components/grid/Col.svelte';
  import Grid from '../_components/grid/Grid.svelte';
  import Row from '../_components/grid/Row.svelte';
</script>

<style>
  section {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    /* border-top: 1px solid var(--silver-darken-10); */
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
  }

  header h1 {
    font-size: 4rem;
    line-height: 4.5rem;
    margin-bottom: var(--space-04);
    /* margin-top: var(--space-07); */
  }

  header p {
    font-size: 1.25rem;
    line-height: 1.5rem;
    margin-bottom: var(--space-09);
  }

  p {
    color: var(--grey-darken-10);
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

  p {
    margin-bottom: 1.5rem;
  }

  dt {
    font-weight: 700;
  }

  dd {
    color: var(--grey-darken-10);
    margin-bottom: 1.5rem;
  }

  .info {
    margin-top: var(--space-10);
  }
</style>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <header>
          <h1>nymea GmbH</h1>
          <p>Development and distribution of hard- and software as well as software applications</p>
        </header>
        <p>Information in accordance with sec. 5 of the Austrian E-Commerce Act, sec. 14 of the Commercial Code, and sec. 63 of the Trade Regulation Act, and disclosure in accordance with sec. 25 of the Media Act</p>
        <p>Legal form: "Gesellschaft mit beschränkter Haftung" (limited liability company under Austrian law)</p>
      </Col>
    </Row>
  <!-- </Grid>
</section>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}> -->
    <Row>
      <!-- <Col>
        <p>Information in accordance with sec. 5 of the Austrian E-Commerce Act, sec. 14 of the Commercial Code, and sec. 63 of the Trade Regulation Act, and disclosure in accordance with sec. 25 of the Media Act</p>
        <p>Legal form: "Gesellschaft mit beschränkter Haftung" (limited liability company under Austrian law)</p>
      </Col> -->
      <!-- <Col middle span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}}> -->
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <dl class="info">
          <dt>Registered Address</dt>
          <dd>High Tech Campus Vienna, Gutheil-Schoder-Gasse 10, 1100 Wien</dd>

          <dt>Managing Directors</dt>
          <dd>Simon Seres, Bernhard Trinnes</dd>

          <dt>Commercial Register No.</dt>
          <dd>FN446282y</dd>

          <dt>Commercial Court</dt>
          <dd>Vienna Commercial Court</dd>
        </dl>
      </Col>
      <!-- <Col middle span={{'xs': 12, 'md': 4}}> -->
      <Col span={{'xs': 12, 'sm': 4, 'md': 4, 'lg': 4, 'xl': 4}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <dl class="info">
          <dt>VAT ID</dt>
          <dd>ATU70200659</dd>

          <dt>Phone</dt>
          <dd>+43 1 9977068</dd>

        </dl>
      </Col>
    </Row>
  </Grid>
</section>
