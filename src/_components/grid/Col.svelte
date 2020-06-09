<script>
  import { createStyle } from '../utils/style.js';

  export let offset = undefined;
  export let span = undefined;
  export let order = undefined;
  export let bottom = false;
  export let middle = false;
  export let top = false;
  export let left = false;
  export let center = false;
  export let right = false;

  $: style = createStyle(style, {
    // '--col-gap': gap,
    '--col-order': order,
    '--col-offset': offset,
    '--col-span': span
  });

  console.log('span', span);
</script>

<style>
  :root {
    --col-offset: 0;
    --col-offset-xs: var(--col-offset);
    --col-offset-sm: var(--col-offset);
    --col-offset-md: var(--col-offset);
    --col-offset-lg: var(--col-offset);
    --col-offset-xl: var(--col-offset);

    --col-span: 12;
    --col-span-xs: var(--col-span);
    --col-span-sm: var(--col-span);
    --col-span-md: var(--col-span);
    --col-span-lg: var(--col-span);
    --col-span-xl: var(--col-span);

    --col-order: 0;
  }

  .col {
    /* background-color: rgb(0, 127, 255, 0.9); */
    box-sizing: border-box;
    flex-direction: column;
    flex: 1;
    /* flex: 1 1 100%; */
    /* flex: 0 1 auto; */
    margin-left: calc((100% / var(--row-cols-xs) * var(--col-offset-xs)) + calc(var(--row-gap-xs) / 2));
    margin-right: calc(var(--row-gap) / 2);
    /* overflow: scroll; */
    /* min-width: 30em;
    max-width: 40em; */
    /* padding: 0 calc(var(--row-gap) / 2); */
  }

  .col.span {
    flex: 0 0 calc((100% / var(--row-cols-xs)) * var(--col-span-xs) - var(--row-gap-xs));
  }

  .col.order {
    order: var(--col-order-xs);
  }

  .col.bottom {
    align-self: flex-end;
  }

  .col.middle {
    align-self: center;
  }

  .col.top {
    align-self: flex-start;
  }

  .col.left {
    text-align: left;
  }

  .col.center {
    text-align: center;
  }

  .col.right {
    text-align: right;
  }

  @media only screen and (min-width: 30em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-sm)) * var(--col-offset-sm)); */
      margin-left: calc((100% / var(--row-cols-xs) * var(--col-offset-xs)) + calc(var(--row-gap-xs) / 2));
      margin-right: calc(var(--row-gap-xs) / 2);
    }

    .col.span-xs {
      flex: 0 0 calc((100% / var(--row-cols-xs)) * var(--col-span-xs) - var(--row-gap-xs));
    }

    .col.order {
      order: var(--col-order-xs);
    }
  }

  @media only screen and (min-width: 48em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-sm)) * var(--col-offset-sm)); */
      margin-left: calc((100% / var(--row-cols-sm) * var(--col-offset-sm)) + calc(var(--row-gap-sm) / 2));
      margin-right: calc(var(--row-gap-sm) / 2);
    }

    .col.span-sm {
      flex: 0 0 calc((100% / var(--row-cols-sm)) * var(--col-span-sm) - var(--row-gap-sm));
    }

    .col.order {
      order: var(--col-order-sm);
    }
  }

  @media only screen and (min-width: 64em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-md)) * var(--col-offset-md)); */
      margin-left: calc((100% / var(--row-cols-md) * var(--col-offset-md)) + calc(var(--row-gap-md) / 2));
      margin-right: calc(var(--row-gap-md) / 2);
    }

    .col.span-md {
      flex: 0 0 calc((100% / var(--row-cols-md)) * var(--col-span-md) - var(--row-gap-md));
    }

    .col.order {
      order: var(--col-order-md);
    }
  }

  @media only screen and (min-width: 75em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-lg)) * var(--col-offset-lg)); */
      margin-left: calc((100% / var(--row-cols-lg) * var(--col-offset-lg)) + calc(var(--row-gap-lg) / 2));
      margin-right: calc(var(--row-gap-lg) / 2);
    }

    .col.span-lg {
      flex: 0 0 calc((100% / var(--row-cols-lg)) * var(--col-span-lg) - var(--row-gap-lg));
    }

    .col.order {
      order: var(--col-order-lg);
    }
  }

  @media only screen and (min-width: 105em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-xl)) * var(--col-offset-xl)); */
      margin-left: calc((100% / var(--row-cols-xl) * var(--col-offset-xl)) + calc(var(--row-gap-xl) / 2));
      margin-right: calc(var(--row-gap-xl) / 2);
    }

    .col.span-xl {
      flex: 0 0 calc((100% / var(--row-cols-xl)) * var(--col-span-xl) - var(--row-gap-xl));
    }

    .col.order {
      order: var(--col-order-xl);
    }
  }
</style>

<div
  class="col"
  class:span={span && span['xs']}
  class:span-xs={span && span['xs']}
  class:span-sm={span && span['sm']}
  class:span-md={span && span['md']}
  class:span-lg={span && span['lg']}
  class:span-xl={span && span['xl']}
  class:order={order}
  class:bottom
  class:middle
  class:top
  class:left
  class:center
  class:right
  {style}
>
  <slot />
</div>
