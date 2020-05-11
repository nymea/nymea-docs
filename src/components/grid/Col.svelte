<script>
  import { createStyle } from '../utils/style.js';

  export let gap;
  export let offset;
  export let span;
  export let middle;

  $: style = createStyle(style, {
    // '--col-gap': gap,
    '--col-offset': offset,
    '--col-span': span
  });
</script>

<style>
  :root {
    /* --col-gap: 0; */
    --col-offset-xs: 0;
    --col-offset-sm: 0;
    --col-offset-md: 0;
    --col-offset-lg: 0;
    --col-offset-xl: 0;
    --col-offset: var(--col-offset-xs);
    /* --col-span: 1; */
  }

  .col {
    /* background-color: rgb(0, 127, 255, 0.9); */
    box-sizing: border-box;
    flex-direction: column;
    flex: 1;
    /* flex: 1 1 100%; */
    /* flex: 0 1 auto; */
    margin-left: calc((100% / var(--row-cols) * var(--col-offset)) + calc(var(--row-gap) / 2));
    margin-right: calc(var(--row-gap) / 2);
    /* min-width: 30em;
    max-width: 40em; */
    /* padding: 0 calc(var(--row-gap) / 2); */
  }

  .col.span {
    flex: 0 0 calc((100% / var(--row-cols)) * var(--col-span));
  }

  .col.middle {
    align-self: center;
  }

  @media only screen and (min-width: 48em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-sm)) * var(--col-offset-sm)); */
      margin-left: calc((100% / var(--row-cols-sm) * var(--col-offset-sm)) + calc(var(--row-gap) / 2));
    }

    .col.span-sm {
      flex: 0 0 calc((100% / var(--row-cols-sm)) * var(--col-span-sm));
    }
  }

  @media only screen and (min-width: 64em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-md)) * var(--col-offset-md)); */
      margin-left: calc((100% / var(--row-cols-md) * var(--col-offset-md)) + calc(var(--row-gap) / 2));
    }

    .col.span-md {
      flex: 0 0 calc((100% / var(--row-cols-md)) * var(--col-span-md));
    }
  }

  @media only screen and (min-width: 75em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-lg)) * var(--col-offset-lg)); */
      margin-left: calc((100% / var(--row-cols-lg) * var(--col-offset-lg)) + calc(var(--row-gap) / 2));
    }

    .col.span-lg {
      flex: 0 0 calc((100% / var(--row-cols-lg)) * var(--col-span-lg));
    }
  }

  @media only screen and (min-width: 105em) {
    .col {
      /* margin-left: calc((100% / var(--row-cols-xl)) * var(--col-offset-xl)); */
      margin-left: calc((100% / var(--row-cols-xl) * var(--col-offset-xl)) + calc(var(--row-gap) / 2));
    }

    .col.span-xl {
      flex: 0 0 calc((100% / var(--row-cols-xl)) * var(--col-span-xl));
    }
  }
</style>

<div
  class="col"
  class:span
  class:span-sm={style['--col-span-sm']}
  class:span-md={style['--col-span-md']}
  class:span-lg={style['--col-span-lg']}
  class:span-xl={style['--col-span-xl']}
  class:middle
  {style}
>
  <slot />
</div>
