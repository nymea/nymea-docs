<script>
  import { url } from '@sveltech/routify';
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  .products {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    border-top: 1px solid var(--silver-darken-10);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
  }

  .products :global(.row .col) {
    padding-bottom: var(--space-09);
  }

  .product {
    border: 1px solid var(--silver-darken-10);
    border-radius: 5px;
    box-shadow:
      0 1.1px 1.1px rgba(0, 0, 0, 0.014),
      0 3px 3px rgba(0, 0, 0, 0.02),
      0 7.2px 7.2px rgba(0, 0, 0, 0.026),
      0 24px 24px rgba(0, 0, 0, 0.04);
    color: var(--text-color);
    display: flex;
    flex-direction: column;
    height: 100%;
    padding: var(--space-07);
    text-decoration: none;
  }

  @media only screen and (min-width: 30em) {
    .product {
      padding: var(--space-09);
    }
  }

  .product h2,
  .product p {
    margin-bottom: var(--space-07);
  }

  .product > p {
    color: var(--grey-darken-10);
  }

  .platforms {
    font-size: 0.8rem;
    /* margin-top: var(--space-07); */
    margin-top: auto;
    /* justify-self: flex-end; */
    overflow: hidden;
  }

  .platforms > p {
    margin: var(--space-04) 0;
  }

  .core-platforms,
  .app-platforms {
    display: flex;
  }

  .core-platforms li,
  .app-platforms li {
    align-items: center;
    display: flex;
    flex-direction: column;
    margin-left: var(--space-07);
  }

  .core-platforms li:first-child,
  .app-platforms li:first-child {
    margin-left: 0;
  }

  .core-platforms span,
  .app-platforms span {
    order: 2;
    text-align: center;
  }

  .core-platforms ion-icon,
  .app-platforms ion-icon {
    order: 1;
    font-size: 3rem;
    margin-bottom: var(--space-04);
  }
</style>

<section class="products">
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col>
        <a href={$url('/documentation/users/installation/core')} class="product">
          <h2>nymea:core</h2>
          <p>The heart of your Smart Home is nymea:core. Normally it runs on a low powered device such as a Raspberry Pi that is permanentely connected to your network. You can also install nymea:core on any standard computer hardware running GNU/Linux.</p>
          <div class="platforms">
            <p>Available for:</p>
            <ul class="core-platforms">
              <li>
                <span>Raspberry Pi</span>
                <ion-icon src="/img/logos/logo-raspberry-pi.svg"></ion-icon>
              </li>
              <li>
                <span>Yocto</span>
                <ion-icon src="/img/logos/logo-yocto.svg"></ion-icon>
              </li>
              <li>
                <span>Debian</span>
                <ion-icon src="/img/logos/logo-debian.svg"></ion-icon>
              </li>
              <li>
                <span>Ubuntu</span>
                <ion-icon src="/img/logos/logo-ubuntu.svg"></ion-icon>
              </li>
            </ul>
          </div>
        </a>
      </Col>
      <Col>
        <a href={$url('/documentation/users/installation/app')} class="product">
          <h2>nymea:app</h2>
          <p>Setup, configure and control your Smart Home with nymea:app. Available for Phones, Tablets and Desktop Computer it lets you interact with your devices from everywhere.</p>
          <div class="platforms">
            <p>Available for:</p>
            <ul class="app-platforms">
              <li>
                <span>Android</span>
                <ion-icon name="logo-android"></ion-icon>
              </li>
              <li>
                <span>iOS&nbsp;& Mac</span>
                <ion-icon name="logo-apple"></ion-icon>
              </li>
              <li>
                <span>Linux</span>
                <ion-icon name="logo-tux"></ion-icon>
              </li>
              <li>
                <span>Windows</span>
                <ion-icon name="logo-windows"></ion-icon>
              </li>
            </ul>
          </div>
        </a>
      </Col>
    </Row>
  </Grid>
</section>
