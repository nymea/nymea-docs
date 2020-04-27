<script>
  import { onMount, afterUpdate } from 'svelte';
  import { stores } from '@sapper/app';
  import { contentScrollTop } from '../stores.js';

  const { page } = stores();

  let headings = [];
  let anchors = [];
  let links = [];
  let scrollPosition = 0;
  let currentHeading;

  $: console.log('ContentNav - $contentScrollTop', $contentScrollTop);

  onMount(() => {
    const content = document.querySelector('.content');
    const header = content.querySelector('header');
    const nav = document.querySelector('.sidebar-content');
    let anchorOffsets = Array.from(document.querySelectorAll('li a')).map((anchor) => window.screenY + anchor.getBoundingClientRect().top);

    // nav.addEventListener('scroll', (event) => {
    //   anchorOffsets = Array.from(document.querySelectorAll('li a')).map((anchor) => window.screenY + anchor.getBoundingClientRect().top);
    //   console.log('ContentNav - nav scroll update', anchorOffsets);
    // });

    scrollPosition = content.scrollTop;
    console.log('ContentNav - content', content);
    console.log('ContentNav - anchorOffsets', anchorOffsets);

    content.addEventListener('scroll', (event) => {
      scrollPosition = event.target.scrollTop;

      const activeHeading = Array.from(headings).find((heading) => {
        console.log('heading', heading, Array.from(heading.classList.values()).find((value) => value === 'active'));
      })
      currentHeading = Array.from(headings).reverse().find((heading, index) => {
        // console.log('ContentNav - heading', scrollPosition > window.screenY + heading.getBoundingClientRect().top);
        if (index === 0) {
          console.log('window.screenY, heading.getBoundingClientRect().top', scrollPosition,window.screenY, heading.getBoundingClientRect().top, header.getBoundingClientRect().height);
        }
        
        return scrollPosition > window.screenY + heading.getBoundingClientRect().top;
      });

      // anchors.forEach((anchor) => {
      //   // const href = anchor.href.split('#')[1];
      //   console.log('anchor.href', anchor.href);
      //   if (activeHeading && anchor.href === activeHeading.id) {
      //     anchor.classList.remove('active');
      //   }
        
      //   if (currentHeading && anchor.href === currentHeading.id) {
      //     anchor.classList.add('active');
      //   }
      // });

      console.log('links', links)

      // links = links.map((link) => {
      //   if (activeHeading && link.link === activeHeading.id) {
      //     link.active = false;
      //   }
      //   if (currentHeading && link.link === currentHeading.id) {
      //     link.active = true;
      //   }
      //   return link;
      // });
      console.log('links', links.map((link) => link.active).join(', '));
    });
  });

  afterUpdate(() => {
    page.subscribe((page) => {
      console.log('ContentNave - page', page, document);

      headings = document.querySelectorAll('h2, h3, h4, h5, h6');

      links = [];
    
      headings.forEach((heading) => {
        heading.id = heading.textContent.toLowerCase().replace(' ', '-');

        console.log(heading.tagName, heading.textContent);

        switch (heading.tagName) {
          case 'H2':
            links.push({
              text: heading.textContent,
              link: `${heading.id}`
            });
            break;
          case 'H3':
            if (!Array.isArray(links[links.length-1])) {
              links.push([]);
            }
            console.log('document.location', document.location);
            links[links.length-1].push({
              text: heading.textContent,
              link: `${heading.id}`
            });
            break;
          // case 'h3':
          //   links.push(heading.textContent);
          //   break;
        }

        // console.log('links', JSON.stringify(links));
      });

      links = [ ...links ];

      // anchors = document.querySelectorAll('li a');
    });
	});
</script>

<style>
  /* :root {
    --nav-list-header-color: #676767;
    --nav-item-color: #202020;
  }

  div {
    height: auto;
    min-height: 100%;
    padding: 0 0 0 3rem;
  }

  p {
    color: var(--nav-list-header-color);
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    margin: 3rem 0 1.5rem;
    text-transform: uppercase;
  }

  ul {
    list-style-type: none;
    margin: 0;
  }

  ul.inset {
    margin-left: 1.5rem;
  }

  a {
    color: #676767;
    font-size: 0.8rem;
    line-height: 1.875rem;
    text-decoration: none;
  }

  a.active {
    text-decoration: underline;
  } */

  /* div {
    border-left: 1px solid #efefef;
    margin: 3.75rem 0 4.5rem;
    padding: 0.75rem 1.5rem;
  }

  p {
    color: #676767;
    font-size: 0.8rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  ul {
    list-style-type: none;
    margin-top: 0.75rem; 
  } */
</style>


<div>
  {#if links.length > 0}
    <p>Contents</p>
  {/if}
  <ul>
    {#each links as link}
      {#if Array.isArray(link)}
      <ul class="inset">
        {#each link as sublink}
          <li><a class={currentHeading && currentHeading.id === sublink.link ? 'active' : ''} href="{$page.path}#{sublink.link}">{sublink.text}</a></li>
        {/each}
      </ul>
      {:else}
      <li><a class={currentHeading && currentHeading.id === link.link ? 'active' : ''} href="{$page.path}#{link.link}">{link.text}</a></li>
      {/if}
    {/each}
  </ul>
</div>
