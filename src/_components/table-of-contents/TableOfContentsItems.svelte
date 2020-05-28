<script>
  import { url } from '@sveltech/routify';

  export let items = [];

  function scrollTo(link) {
    const element = document.getElementById(link);
    const style = window.getComputedStyle(element);
    const headerHeight = parseFloat(style.getPropertyValue('--header-height').replace('rem', ''));
    const yOffset = (headerHeight + 1.5) * parseFloat(getComputedStyle(document.documentElement).fontSize);
    const y = element.getBoundingClientRect().top + window.pageYOffset - yOffset;

    window.scrollTo({top: y, behavior: 'smooth'});

    // if(window.history.pushState) {
    //   window.history.pushState(null, null, '#' + link);
    // } else {
    //   window.location.hash = '#' + link;
    // }
  }
</script>

<style>
  ul > li > :global(ul) {
    margin-left: 0.85em;
  }

  a {
    /* color: var(--text-color); */
    color: var(--grey-base);
    /* position: relative; */
    text-decoration: none;
  }

  a::before {
    content: "#\00a0";
    color: var(--silver-darken-20);
    /* position: absolute;
      left: -1em; */
  }

  a:hover {
    color: var(--text-color);
    text-decoration: underline;
  }

  a:hover::before {
    color: var(--green-base);
    display: inline-block;
    text-decoration: none;
  }
</style>

<!-- <pre>{JSON.stringify(items)}</pre> -->

<ul class="toc">
  {#each items as item, index}
    {#if !Array.isArray(item)}
      <li>
        <!-- <a href={"#" + $url(item.link)} on:click|preventDefault={() => scrollTo(item.link)}>{item.text}</a> -->
        <a href={"#" + $url(item.link)}>{item.text}</a>
        {#if index + 1 < items.length && Array.isArray(items[index + 1])}
          <svelte:self items={items[index + 1]} />
        {/if}
      </li>
    {/if}

    <!-- <li>
      {#if Array.isArray(item)}
        <svelte:self items={item} />
      {:else}
        <a href={$url(item.link)}>{item.text}</a>
      {/if}
    </li> -->
  {/each}
</ul>
