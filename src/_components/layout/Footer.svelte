<script>
  import { url } from '@sveltech/routify';
  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';
</script>

<style>
  footer {
    background-color: var(--white);
    border-top: 1px solid var(--silver-darken-10);
    padding: 3rem;
    position: relative;
    z-index: 4;
  }

  nav {
    /* background-color: var(--silver-base); */
    /* padding: 1.5rem; */
  }

  ul > li > ul > li {

  }
</style>

<footer>
  <!-- <Grid>
    <Row>
      <Col span={{'xs': 8, 'sm': 8, 'md': 8, 'lg': 8, 'xl': 8}}> -->
        <nav>
          <ul class="menu">
            <li>
              <a href={$url('/users')}>Users</a>
            </li>
            <li>
              <a href={$url('/developers')}>Developers</a>
            </li>
            <li>
              <a href={$url('/businesses')}>Businesses</a>
            </li>
            <li>
              <a href={$url('/documentation/overview')}>Documentation</a>
              <ul class="menu">
                <li>
                  <a href={$url('/documentation/overview')}>Overview</a>
                </li>
                <li>
                  <a href={$url('/documentation/users/installation/app')}>Users</a>
                </li>
                <li>
                  <a href={$url('/documentation/developers')}>Developers</a>
                </li>
              </ul>
            </li>
            <li>
              <a href={$url('/imprint')}>Imprint</a>
            </li>
          </ul>
        </nav>
      <!-- </Col>
    </Row>
  </Grid> -->
  <!-- <slot /> -->
</footer>
