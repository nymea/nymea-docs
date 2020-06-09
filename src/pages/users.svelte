<script>
  import Col from '../_components/grid/Col.svelte';
  import Row from '../_components/grid/Row.svelte';
  import FeaturesSection from '../_components/sections/FeaturesSection.svelte';
  import HighlightSection from '../_components/sections/HighlightSection.svelte';
  import IntegrationsSection from '../_components/sections/IntegrationsSection.svelte';
  import IntroductionSection from '../_components/sections/IntroductionSection.svelte';
  import LogosSection from '../_components/sections/LogosSection.svelte';
  import ProductsSection from '../_components/sections/ProductsSection.svelte';
  import ShowcasesSection from '../_components/sections/ShowcasesSection.svelte';
</script>

<style></style>

<IntroductionSection
  title="Live smart."
  subTitle="Nymea gets you up and running with your Smart Home setup in no time."
  buttonText="Get started",
  buttonLink="./documentation/users/installation/getting-started" />

<!-- <HighlightSection>
  <Row>
    <Col span={{'xs': 12, 'md': 5, 'lg': 5, 'xl': 5}}>
      <div class="product">
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
              <span>Ubuntu</span>
              <ion-icon src="/img/logos/logo-debian.svg"></ion-icon>
            </li>
            <li>
              <span>Debian</span>
              <ion-icon src="/img/logos/logo-ubuntu.svg"></ion-icon>
            </li>
          </ul>
        </div>
      </div>
    </Col>
    <Col span={{'xs': 12, 'md': 5, 'lg': 5, 'xl': 5}} offset={{'xs': 0, 'md': 2, 'lg': 2, 'xl': 2}}>
      <div class="product">
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
              <span>Ubuntu (Touch)</span>
              <ion-icon src="/img/logos/logo-ubuntu.svg"></ion-icon>
            </li>
            <li>
              <span>Windows</span>
              <ion-icon name="logo-windows"></ion-icon>
            </li>
          </ul>
        </div>
      </div>
    </Col>
  </Row>
</HighlightSection> -->

<FeaturesSection />

<IntegrationsSection />

<ProductsSection />

<ShowcasesSection />

<LogosSection />
