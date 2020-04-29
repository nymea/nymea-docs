<script></script>

<style>
  ul {
    /* display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
    list-style-type: none; */

    /* display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    margin: calc(0.75rem * -1); */
    /* padding: 0 0 0 0.75rem; */
    list-style-type: none;

    display: grid;
    grid-gap: 1.5rem;
    grid-template-columns: repeat(auto-fill, minmax(16rem, 1fr));
    margin-bottom: 3rem;
  }

  /* ul::after {
    content: "";
    flex-grow: 1;
    flex-shrink: 0;
    flex-basis: calc((30rem - 100%) * 999);
  } */
</style>

<ul>
  <slot></slot>
</ul>