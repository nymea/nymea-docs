<script></script>

<style>
  li {
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