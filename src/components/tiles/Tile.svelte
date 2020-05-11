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
    flex-basis: 32%;
    margin-bottom: 2%;
    margin-left: 2%;
    padding: 1.5rem;
  }

  li:nth-child(3n+1) {
    margin-left: 0;
  }
</style>

<li class="tile">
  <slot></slot>
</li>