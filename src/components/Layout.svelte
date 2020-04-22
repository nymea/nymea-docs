<script>
  import { contentScrollTop } from '../stores.js';

  export let dir = 'ltr';
  export let sidebarPageWidth = '20rem';
  export let sidebarContentWidth = '20rem';

  // function handleScroll(event) {
  //   console.log('handleScroll', event);

  //   // const scrollPosition = window.scrollTop();

  //   contentScrollTop.update((scrollTop) => scrollTop = event.target.scrollTop);

  //   console.log('scrollPosition', event.target.scrollTop);
  // }
</script>

<style>
  :root {
    --sidebar-wrapper-vertical-padding: 0rem;
    /* --sidebar-background-color: #fafafa; */
    --sidebar-background-color: transparent;
    --sidebar-border-color: #efefef;
    --sidebar-padding: 0rem;
    --content-background-color: #fff;
    --content-padding: 0rem;
  }

  .layout {
    display: flex;
    flex-wrap: wrap;
    min-height: 100vh;
  }

  .layout.ltr {
    flex-direction: row;
  }

  .layout.ltr .sidebar-page {
    justify-content: flex-end;
  }

  .layout.ltr .sidebar-content {
    justify-content: flex-start;
  }

  .layout.rtl {
    flex-direction: row-reverse;
  }

  .layout.rtl .sidebar-page {
    justify-content: flex-start;
  }

  .layout.rtl .sidebar-content {
    justify-content: flex-end;
  }


  .sidebar-page {
    background-color: var(--sidebar-background-color);
    display: flex;
    flex-basis: var(--sidebar-page-width);
    flex-grow: 1;
    height: 100vh;
    overflow: scroll;
    padding: var(--sidebar-padding);
  }

  .content {
    /* border-left: 1px solid #efefef;
    border-right: 1px solid #efefef; */
    flex-basis: 0;
    flex-grow: 999;
    height: 100vh;
    overflow: scroll;
    padding: var(--content-padding);
  }
  
  .sidebar-content {
    background-color: var(--sidebar-background-color);
    display: flex;
    flex-basis: var(--sidebar-content-width);
    flex-grow: 1;
    height: 100vh;
    overflow: scroll;
    padding: var(--sidebar-padding);
  }
</style>

<div class="layout {dir}">
  <div class="sidebar-page" style="--sidebar-page-width: {sidebarPageWidth}">
    <slot name="sidebar-page"></slot>
  </div>
  
  <!-- <div class="content" on:scroll={handleScroll}> -->
  <div class="content">
    <slot name="content"></slot>
  </div>
  
  <div class="sidebar-content" style="--sidebar-content-width: {sidebarContentWidth}">
    <slot name="sidebar-content"></slot>
  </div>
</div>
