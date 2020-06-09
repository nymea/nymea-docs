<script>
  import { createStyle } from '../utils/style.js';

  import Col from '../grid/Col.svelte';
  import Grid from '../grid/Grid.svelte';
  import Row from '../grid/Row.svelte';

  export let position = undefined;
  export let width = undefined;
  export let contentOffset = undefined;
  export let contentSpan = undefined;
  export let siderOffset = undefined;
  export let siderSpan = undefined;
  export let contentWrapperMargin = undefined;
  export let leftBackground = undefined;
  export let rightBackground = undefined;

  $: style = createStyle(style, {
    '--layout-position': getJustifyContent(position),
    '--layout-width': width,
    '--layout-content-offset': contentOffset,
    '--layout-content-span': contentSpan,
    '--layout-sider-offset': siderOffset,
    '--layout-sider-span': siderSpan,
    '--layout-content-wrapper-margin': contentWrapperMargin,
    '--layout-left-background': leftBackground,
    '--layout-right-background': rightBackground,
  });

  function getJustifyContent(position) {
    if (position === 'start' || position === 'end') {
      return `flex-${position}`;
    } else {
      return 'center';
    }
  }
</script>

<style>
  :root {
    --layout-position: center;
    --layout-width: 100%;
    --layout-width-xs: var(--layout-width);
    --layout-width-sm: var(--layout-width);
    --layout-width-md: var(--layout-width);
    --layout-width-lg: var(--layout-width);
    --layout-width-xl: var(--layout-width);

    --layout-content-offset: 0;
    --layout-content-offset-xs: var(--layout-content-offset);
    --layout-content-offset-sm: var(--layout-content-offset);
    --layout-content-offset-md: var(--layout-content-offset);
    --layout-content-offset-lg: var(--layout-content-offset);
    --layout-content-offset-xl: var(--layout-content-offset);

    --layout-content-span: 8;
    --layout-content-span-xs: var(--layout-content-span);
    --layout-content-span-sm: var(--layout-content-span);
    --layout-content-span-md: var(--layout-content-span);
    --layout-content-span-lg: var(--layout-content-span);
    --layout-content-span-xl: var(--layout-content-span);

    --layout-sider-offset: 0;
    --layout-sider-offset-xs: var(--layout-sider-offset);
    --layout-sider-offset-sm: var(--layout-sider-offset);
    --layout-sider-offset-md: var(--layout-sider-offset);
    --layout-sider-offset-lg: var(--layout-sider-offset);
    --layout-sider-offset-xl: var(--layout-sider-offset);

    --layout-sider-span: 4;
    --layout-sider-span-xs: var(--layout-sider-span);
    --layout-sider-span-sm: var(--layout-sider-span);
    --layout-sider-span-md: var(--layout-sider-span);
    --layout-sider-span-lg: var(--layout-sider-span);
    --layout-sider-span-xl: var(--layout-sider-span);

    --layout-content-wrapper-margin: 0;

    --layout-left-background: var(--white);
    --layout-right-background: var(--white);
  }

  .outer-wrapper {
    display: flex;
    flex-direction: column;
    align-items: var(--layout-position);
    position: relative;
  }

  .outer-wrapper::before,
  .outer-wrapper::after {
    content: "";
    position: fixed;
      bottom: 0;
      top: var(--header-height);
    z-index: 0;
  }

  @media only screen and (min-width: 48em) {
    .outer-wrapper::before {
      /* background-color: var(--white); */
      background: var(--layout-left-background);
      left: 0;
      right: 50%;
    }

    .outer-wrapper::after {
      /* background: linear-gradient(to bottom, var(--silver-base), var(--white)); */
      background: var(--layout-right-background);
      left: 50%;
      right: 0;
    } 
  }
  .outer-wrapper > .inner-wrapper {
    width: var(--layout-width);
    z-index: 1;
  }

  .content-wrapper {
    background-color: var(--white);
    display: flex;
    flex-direction: column;
    /* margin: 0 calc(var(--row-gap) / 2); */
    margin: 0 var(--layout-content-wrapper-margin);
  }


  .layout > :global([slot="header"]),
  .layout > :global([slot="footer"]),
  .content-wrapper > :global([slot="content"] > .content) {
    width: 100%;
  }

  .content-wrapper > :global([slot="content"]) {
    display: flex;
  }

  .content-wrapper > :global([slot="content"]) {
    /* padding-left: var(--layout-content-offset); */
    /* padding-left: calc((100% / var(--row-cols)) * var(--layout-content-offset) + calc(var(--row-gap) / 2));; */
    /* padding-left: calc((100% / var(--row-cols)) * var(--layout-content-offset) + (var(--row-gap) / 2));
    padding-right: calc(var(--row-gap) / 2); */
    min-width: 0;     /* Solves issue with <pre></pre> tags when there are large code blocks in there. https://weblog.west-wind.com/posts/2016/feb/15/flexbox-containers-pre-tags-and-managing-overflow */
    /* flex-basis: var(--content-width); */
    flex-basis: calc((100% / var(--row-cols)) * var(--layout-content-span) - var(--row-gap));
  }

  .content-wrapper > :global([slot="sider"]) {
    /* padding-left: var(--sider-offset); */
    padding-left: calc((100% / var(--row-cols)) * var(--layout-sider-offset) + calc(var(--row-gap)));
    /* flex-basis: var(--sider-width); */
    flex-basis: calc((100% / var(--row-cols)) * var(--layout-sider-span) - var(--row-gap));
    /* width: calc((100% / var(--row-cols)) * var(--layout-sider-span) - var(--row-gap)); */
    width: initial;
  }

  @media only screen and (min-width: 30em) {

    .outer-wrapper > .inner-wrapper {
      width: var(--layout-width-xs);
    }
    .content-wrapper {
      /* margin: 0 calc(var(--row-gap-xs) / 2); */
    }

    .content-wrapper > :global([slot="content"]) {
      /* padding-left: calc((100% / var(--row-cols-xs)) * var(--layout-content-offset-xs) + calc(var(--row-gap-xs) / 2));; */
      /* padding-left: calc((100% / var(--row-cols-xs)) * var(--layout-content-offset-xs) + (var(--row-gap-xs) / 2));
      padding-right: calc(var(--row-gap-xs) / 2); */
      flex-basis: calc((100% / var(--row-cols-xs)) * var(--layout-content-span-xs) - var(--row-gap-xs));
    }

    .content-wrapper > :global([slot="sider"]) {
      padding-left: calc((100% / var(--row-cols-xs)) * var(--layout-sider-offset-xs) + calc(var(--row-gap-xs)));
      flex-basis: calc((100% / var(--row-cols-xs)) * var(--layout-sider-span-xs) - var(--row-gap-xs));
      /* width: calc((100% / var(--row-cols-xs)) * var(--layout-sider-span-xs) - var(--row-gap-xs)); */
    }
  }

  @media only screen and (min-width: 48em) {

    .outer-wrapper > .inner-wrapper {
      width: var(--layout-width-sm);
    }
    .content-wrapper {
      /* margin: 0 calc(var(--row-gap-sm) / 2); */
    }

    .content-wrapper > :global([slot="content"]) {
      /* padding-left: calc((100% / var(--row-cols-sm)) * var(--layout-content-offset-sm) + calc(var(--row-gap-sm) / 2)); */
      /* padding-left: calc((100% / var(--row-cols-sm)) * var(--layout-content-offset-sm) + (var(--row-gap-sm) / 2));
      padding-right: calc(var(--row-gap-sm) / 2); */
      flex-basis: calc((100% / var(--row-cols-sm)) * var(--layout-content-span-sm) - var(--row-gap-sm));
    }

    .content-wrapper > :global([slot="sider"]) {
      padding-left: calc((100% / var(--row-cols-sm)) * var(--layout-sider-offset-sm) + calc(var(--row-gap-sm)));
      flex-basis: calc((100% / var(--row-cols-sm)) * var(--layout-sider-span-sm) - var(--row-gap-sm));
      /* width: calc((100% / var(--row-cols-sm)) * var(--layout-sider-span-sm) - var(--row-gap-sm)); */
    }
  }

  @media only screen and (min-width: 64em) {
    .outer-wrapper > .inner-wrapper {
      width: var(--layout-width-md);
    }

    .content-wrapper {
      flex-direction: row;
      /* margin: 0 calc(var(--row-gap-md) / 2); */
    }

    .content-wrapper > :global([slot="content"]) {
      /* padding-left: calc((100% / var(--row-cols-md)) * var(--layout-content-offset-md) + calc(var(--row-gap-md) / 2)); */
      /* padding-left: calc((100% / var(--row-cols-md)) * var(--layout-content-offset-md) + (var(--row-gap-md) / 2));
      padding-right: calc(var(--row-gap-md) / 2); */
      flex-basis: calc((100% / var(--row-cols-md)) * var(--layout-content-span-md) - var(--row-gap-md));
    }

    .content-wrapper > :global([slot="sider"]) {
      flex-shrink: 0;
      padding-left: calc((100% / var(--row-cols-md)) * var(--layout-sider-offset-md) + calc(var(--row-gap-md)));
      flex-basis: calc((100% / var(--row-cols-md)) * var(--layout-sider-span-md) - var(--row-gap-md));
      /* width: calc((100% / var(--row-cols-md)) * var(--layout-sider-span-md) - var(--row-gap-md)); */
    }
  }

  @media only screen and (min-width: 75em) {
    .outer-wrapper > .inner-wrapper {
      width: var(--layout-width-lg);
    }

    .content-wrapper {
      /* margin: 0 calc(var(--row-gap-lg) / 2); */
    }

    .content-wrapper > :global([slot="content"]) {
      /* padding-left: calc((100% / var(--row-cols-lg)) * var(--layout-content-offset-lg) + calc(var(--row-gap-lg) / 2)); */
      /* padding-left: calc((100% / var(--row-cols-lg)) * var(--layout-content-offset-lg) + (var(--row-gap-lg) / 2));
      padding-right: calc(var(--row-gap-lg) / 2); */
      flex-basis: calc((100% / var(--row-cols-lg)) * var(--layout-content-span-lg) - var(--row-gap-lg));
    }

    .content-wrapper > :global([slot="sider"]) {
      padding-left: calc((100% / var(--row-cols-lg)) * var(--layout-sider-offset-lg) + calc(var(--row-gap-lg)));
      flex-basis: calc((100% / var(--row-cols-lg)) * var(--layout-sider-span-lg) - var(--row-gap-lg));
      /* width: calc((100% / var(--row-cols-lg)) * var(--layout-sider-span-lg) - var(--row-gap-lg)); */
    }
  }

  @media only screen and (min-width: 105em) {
    .outer-wrapper > .inner-wrapper {
      width: var(--layout-width-xl);
    }

    .content-wrapper {
      /* margin: 0 calc(var(--row-gap-xl) / 2); */
    }

    .content-wrapper > :global([slot="content"]) {
      /* padding-left: calc((100% / var(--row-cols-xl)) * var(--layout-content-offset-xl) + calc(var(--row-gap-xl) / 2)); */
      /* padding-left: calc((100% / var(--row-cols-xl)) * var(--layout-content-offset-xl) + (var(--row-gap-xl) / 2));
      padding-right: calc(var(--row-gap-xl) / 2); */
      /* flex-basis: calc((100% / var(--row-cols-xl)) * var(--layout-content-span-xl) - var(--row-gap-xl)); */
      flex-basis: calc((100% / var(--row-cols-xl)) * var(--layout-content-span-xl));
    }

    .content-wrapper > :global([slot="sider"]) {
      padding-left: calc((100% / var(--row-cols-xl)) * var(--layout-sider-offset-xl) + calc(var(--row-gap-xl)));
      flex-basis: calc((100% / var(--row-cols-xl)) * var(--layout-sider-span-xl) - var(--row-gap-xl));
      /* width: calc((100% / var(--row-cols-xl)) * var(--layout-sider-span-xl) - var(--row-gap-xl)); */
    }
  }
</style>

<slot name="header" />
<div class="layout outer-wrapper" {style}>
  <div class="layout inner-wrapper">
    <div class="layout content-wrapper">
      <slot name="content" />
      <slot name="sider" />
    </div>
    <slot name="footer" />
  </div>
</div>
