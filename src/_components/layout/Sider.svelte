<script>

</script>

<style>
  :root {
    --sider-background: linear-gradient(to bottom, var(--silver-base), var(--white));
    --sider-border-background: linear-gradient(to bottom, var(--silver-darken-10), var(--white));
    --sider-height: 100%;
  }

  div {
    height: var(--sider-height);
  }

  .sider {
    background: var(--sider-background);
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: var(--sider-height);
    overflow-x: hidden;
    overflow-y: auto;
    padding-right: 999em;
    margin-right: -999em;
    /* padding-right: (var(--row-gap) / 2); */
    position: fixed;
      left: calc((100% - var(--layout-width)) / 2 + (var(--row-gap) / 2) + (var(--layout-width) - var(--row-gap)) / var(--row-cols) * var(--layout-content-span) + (var(--row-gap) / 2));
      right: calc((100% - var(--layout-width)) / 2 + (var(--row-gap) / 2));
    z-index: 0;
  }

  /* @media only screen and (min-width: 30em) {
    .sider {
      padding-right: (var(--row-gap-xs) / 2);
      left: calc((100% - var(--layout-width-xs)) / 2 + (var(--row-gap-xs) / 2) + (var(--layout-width-xs) - var(--row-gap-xs)) / var(--row-cols-xs) * var(--layout-content-span-xs) + (var(--row-gap-xs) / 2));
      right: calc((100% - var(--layout-width-xs)) / 2 + (var(--row-gap-xs) / 2));
    }
  }

  @media only screen and (min-width: 48em) {
    .sider {
      padding-right: (var(--row-gap-sm) / 2);
      left: calc((100% - var(--layout-width-sm)) / 2 + (var(--row-gap-sm) / 2) + (var(--layout-width-sm) - var(--row-gap-sm)) / var(--row-cols-sm) * var(--layout-content-span-sm) + (var(--row-gap-sm) / 2));
      right: calc((100% - var(--layout-width-sm)) / 2 + (var(--row-gap-sm) / 2));
    }
  }

  @media only screen and (min-width: 64em) {
    .sider {
      padding-right: (var(--row-gap-md) / 2);
      left: calc((100% - var(--layout-width-md)) / 2 + (var(--row-gap-md) / 2) + (var(--layout-width-md) - var(--row-gap-md)) / var(--row-cols-md) * var(--layout-content-span-md) + (var(--row-gap-md) / 2));
      right: calc((100% - var(--layout-width-md)) / 2 + (var(--row-gap-md) / 2));
    }
  }

  @media only screen and (min-width: 75em) {
    .sider {
      padding-right: (var(--row-gap-lg) / 2);
      left: calc((100% - var(--layout-width-lg)) / 2 + (var(--row-gap-lg) / 2) + (var(--layout-width-lg) - var(--row-gap-lg)) / var(--row-cols-lg) * var(--layout-content-span-lg) + (var(--row-gap-lg) / 2));
      right: calc((100% - var(--layout-width-lg)) / 2 + (var(--row-gap-lg) / 2));
    }
  } */

  @media only screen and (min-width: 105em) {
    .sider {
      padding-right: (var(--row-gap-xl) / 2);
      left: calc((100% - var(--layout-width-xl)) / 2 + (var(--row-gap-xl) / 2) + (var(--layout-width-xl) - var(--row-gap-xl)) / var(--row-cols-xl) * var(--layout-content-span-xl) + (var(--row-gap-xl) / 2));
      right: calc((100% - var(--layout-width-xl)) / 2 + (var(--row-gap-xl) / 2));
    }
  }

  .sider::before {
    background: var(--sider-border-background);
    content: "";
    position: fixed;
      bottom: 0;
      /* left: 0; */
      top: 0;
    width: 1px;
    z-index: 1;
  }
</style>

<div>
  <aside class="layout sider">
    <slot />
  </aside>
</div>
