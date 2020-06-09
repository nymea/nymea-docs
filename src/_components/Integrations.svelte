<script>
  export let items = [
    {
      link: 'documentation/overview/integrations?category=light',
      icon: 'bulb',
      title: 'Lights'
    },
  ];
  export let itemCount = -1;
  export let more = true;
</script>

<style>
  .integrations {
    box-sizing: border-box;
    display: flex;
    /* height: 6.375rem; */
    justify-content: space-between;
    overflow-x: hidden;
    width: 100%;
  }

  /* .integrations.more {
    padding-right: var(--space-10);
    position: relative;
  } */

  /* .integrations.more li:last-child {
    position: absolute;
    right: 0;
  } */

  .integration {
    color: var(--text-color);
    display: block;
    flex: 1 1 0;
    height: 100%;
    min-width: var(--space-10);
    padding: var(--space-04);
    text-align: center;
    text-decoration: none;
    /* width: 6.375rem; */
  }

  /* .integrations li:nth-child(3), */
  .integrations li:nth-child(4),
  .integrations li:nth-child(5),
  .integrations li:nth-child(6),
  .integrations li:nth-child(7),
  .integrations li:nth-child(8) {
  /* .integrations li:nth-child(9) { */
    display: none;
  }

  .integration ion-icon {
    color: var(--text-color);
    font-size: 2.25rem;
    line-height: 3rem;
    margin-bottom: 0.75rem;
  }

  .integration h6 {
    margin: 0;
    overflow-wrap: break-word;
    hyphens: auto;
    word-wrap: break-word;
  }

  @media only screen and (min-width: 30em) {
    .integrations li:nth-child(4) {
      display: block;
    }
  }

  @media only screen and (min-width: 48em) {
    .integrations li:nth-child(5),
    .integrations li:nth-child(6) {
      display: block;
    }
  }

  @media only screen and (min-width: 64em) {
    .integrations li:nth-child(7),
    .integrations li:nth-child(8) {
      display: block;
    }
  }
</style>

<ul class="integrations">
  <li>
    <a href="documentation/overview/integrations?category=light" class="integration">
      <ion-icon name="bulb"></ion-icon>
      <h6>Lights</h6>
    </a>
  </li>
  <li>
    <a href="documentation/overview/integrations?category=sensor" class="integration">
      <ion-icon name="thermometer"></ion-icon>
      <h6>Sensors</h6>
    </a>
  </li>
  <li>
    <a href="documentation/overview/integrations?category=lock" class="integration">
      <ion-icon name="key"></ion-icon>
      <h6>Access control</h6>
    </a>
  </li>
  <li>
    <a href="documentation/overview/integrations?category=weather" class="integration">
      <ion-icon name="partly-sunny"></ion-icon>
      <h6>Weather</h6>
    </a>
  </li>
  <li>
    <a href="documentation/overview/integrations?category=multimedia" class="integration">
      <ion-icon name="play"></ion-icon>
      <h6>Media</h6>
    </a>
  </li>
<!-- </ul>
<ul class="integrations"> -->
  <li>
    <a href="documentation/overview/integrations?category=tool,sensor" class="integration">
      <ion-icon name="water"></ion-icon>
      <h6>Irrigation</h6>
    </a>
  </li>
  <li>
    <a href="documentation/overview/integrations?category=notification" class="integration">
      <ion-icon name="notifications"></ion-icon>
      <h6>Notifications</h6>
    </a>
  </li>
  <li>
    <a href="documentation/overview/integrations?category=online-service" class="integration">
      <ion-icon name="location"></ion-icon>
      <h6>Presence Awareness</h6>
    </a>
  </li>
  {#if more}
    <li>
      <a href="documentation/overview/integrations" class="integration">
        <ion-icon name="ellipsis-horizontal"></ion-icon>
        <h6>Many More</h6>
      </a>
    </li>
  {/if}
</ul>
