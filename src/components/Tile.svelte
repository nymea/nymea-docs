<script></script>

<style>
  li {
    /* box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05), 
                0 2px 4px rgba(0, 0, 0, 0.05), 
                0 4px 8px rgba(0, 0, 0, 0.05), 
                0 8px 16px rgba(0, 0, 0, 0.05), 
                0 16px 32px rgba(0, 0, 0, 0.05); */
    border: 1px solid #efefef;
    border-radius: 6px;
    display: block;
    height: 100%;
    /* flex-basis: 32%;
    margin-bottom: 2%;
    margin-left: 2%; */
    /* flex: 1 1 calc(12rem + 0.75rem);
    margin-bottom: 1.5rem;
    padding: 1.5rem; */

    /* flex-grow: 1;
    flex-basis: calc((30rem - 100%) * 999);
    margin: 0.75rem;
    min-width: 16rem; */
    padding: 1.5rem;
    /* max-width: calc(20% - 1.5rem); */
  }

  /* li:nth-child(3n+1) {
    margin-left: 0;
  } */
</style>

<li class="tile">
  <slot></slot>
</li>