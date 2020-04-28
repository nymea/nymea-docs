<script>
  export let orientation = 'left';
  export let width = '20rem';
</script>

<style>
  :root {
    --sidebar-wrapper-vertical-padding: 0rem;
    --sidebar-background-color: #fafafa;
    --sidebar-border-color: #efefef;
    --sidebar-padding: 1.5rem;
    /* --sidebar-width: 20rem; */
    --content-background-color: #fff;
  }

  .sidebar-wrapper {
    display: flex;
    flex-wrap: wrap;
    min-height: 100vh;
    padding: var(--sidebar-wrapper-vertical-padding) 0;
  }

  .sidebar-wrapper.left {
    flex-direction: row;
  }

  .sidebar-wrapper.right {
    flex-direction: row-reverse;
  }

  .sidebar {
    background-color: var(--sidebar-background-color);
    flex-basis: var(--sidebar-width);
    flex-grow: 1;
    padding: var(--sidebar-padding);
  }

  .sidebar-wrapper.left .sidebar {
    border-left: 0;
    border-right: 1px solid var(--sidebar-border-color);
  }

  .sidebar-wrapper.right .sidebar {
    border-left: 1px solid var(--sidebar-border-color);
    border-right: 0;
  }

  .content {
    /* background-color: var(--content-background-color); */
    flex-basis: 0;
    flex-grow: 999;
  }
</style>

<div class="sidebar-wrapper {orientation}">
  <div class="sidebar" style="--sidebar-width: {width}">
    <slot name="sidebar"></slot>
  </div>
  <div class="content">
    <slot name="content"></slot>
  </div>
</div>
