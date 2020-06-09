<script>
  import Col from '../_components/grid/Col.svelte';
  import Row from '../_components/grid/Row.svelte';
  import IntroductionSection from '../_components/sections/IntroductionSection.svelte';
  import HighlightSection from '../_components/sections/HighlightSection.svelte';
  import OffersSection from '../_components/sections/OffersSection.svelte';
  import PartnersSection from '../_components/sections/PartnersSection.svelte';
  import Section from '../_components/sections/Section.svelte';
</script>

<style>
  h2 {
    margin-bottom: var(--space-07);
  }

  h2 + p {
    color: var(--grey-base);
    font-size: 1.125rem;
  }
</style>

<IntroductionSection
  title="Build smart."
  subTitle="Build IoT business, not IoT devices."
  buttonText="Get started",
  buttonLink="./documentation/developers"
  showButton="false" />

<OffersSection />

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>'Works with'</h2>
      <p>Interoperability is the key success factor. By installing nymea you make your device compatible to virtually anything, saving thousands of integration hours.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>The worlds smallest footprint</h2>
      <p>A powerful, yet lean addon for your device firmware. Nymea does not require a power house, it's perfectly fine with low cost modules as long as GNU/Linux is available for them.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Software</h2>
      <p>Nymea is ready to be integrated on a variety of GNU/Linux based devices. Be it Yocto, Ubuntu Core, Debian or anything else, we've got the experience in delivering the nymea stack to the OS of your choice.</p>
    </Col>
  </Row>
</Section>

<Section>
  <Row>
    <Col span={{'xs': 12, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}} offset={{'xs': 0, 'sm': 2, 'md': 2, 'lg': 2, 'xl': 2}}>
      <h2>Also need hardware?</h2>
      <p>Together with our partners we can deliver well maintained plug-n-play modules that basically eliminate all the development risks.</p>
    </Col>
  </Row>
</Section>

<PartnersSection />