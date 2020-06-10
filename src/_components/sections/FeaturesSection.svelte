<script>
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
  import Integrations from '../Integrations.svelte';
</script>

<style>
  .features {
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-09) + var(--space-07)) 0 var(--space-10);
  }

  @media only screen and (min-width: 64em) {
    .features {
      padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
    }
  }

  .feature {
    margin-top: var(--space-09);
  }

  .features > :global(.grid > .row > .col:first-child .feature) {
    margin-top: 0;
  }

  @media only screen and (min-width: 64em) {
    .feature {
      margin-top: 0;
    }
  }

  .feature header {
    margin-bottom: var(--space-07);
  }

  .feature header ion-icon {
    /* color: var(--turquoise-darken-20); */
    color: var(--text-color);
    font-size: 1.875rem;
    line-height: 3rem;
    margin-bottom: 1.25rem;
  }

  .feature header h3 {
    margin-bottom: 0.25rem;
  }

  .feature header p {
    color: var(--turquoise-darken-20);
    /* color: var(--grey-base); */
    /* color: var(--text-color); */
    font-size: 0.8rem;
    letter-spacing: 0.01em;
    text-transform: uppercase;
  }

  .feature header + p {
    color: var(--grey-darken-10);
  }
</style>

<section class="features">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 4}}>        
        <div class="feature">
          <header>
            <ion-icon name="body"></ion-icon>
            <h3>Focused on usability</h3>
            <!-- <p>Never touch a console again</p> -->
          </header>
          <p>Nymea does not require editing cryptic configuration files, it can be configured and controlled entirely using your Smartphone or PC.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="feature">
          <header>
            <ion-icon name="shield-checkmark"></ion-icon>
            <h3>Local-first</h3>
            <!-- <p>Keep in control of your data</p> -->
          </header>
          <p>Nymea ensures that your data is kept where it belongs, locally in your home. Besides the privacy advantage, this also keeps you independent from cloud vendors, and doesn't require an always-on internet connection.</p>
        </div>
      </Col>
      <Col span={{'xs': 12, 'sm': 4}}>
        <div class="feature">
          <header>
            <ion-icon src="img/open-source-initiative.svg"></ion-icon>
            <h3>Free and Open Source</h3>
            <!-- <p>Transparent functionality</p> -->
          </header>
          <p>Nymea is comitted to open source software. Anything we do can be inspected, tuned and shared by our community.</p>
        </div>
      </Col>
    </Row>
  </Grid>
</section>
