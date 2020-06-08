<script>
  import { onMount } from 'svelte';
  import { beforeUrlChange, url } from '@sveltech/routify'
  import TableOfContentsItems from './TableOfContentsItems.svelte';
  
  let items = [];

  onMount(() => {
    console.log('items', items, items.length);
    initItems();

    // setTimeout(function() {
    //   scrollToHash();
    // }, 300);
  });

  // $beforeUrlChange((event, store) => {
  //   console.log('$beforeUrlChange');
  //   scrollToHash();
  //   return false;
  // });

  function scrollToHash() {
    if (location.hash) {
      /* we need to scroll to the top of the window first, because the browser will always jump to the anchor first before JavaScript is ready, thanks Stack Overflow: http://stackoverflow.com/a/3659116 */
      window.scrollTo(0, 0);

      const target = location.hash.split('#');
      const element = document.getElementById(target[1]);
      const style = window.getComputedStyle(element);
      const headerHeight = parseFloat(style.getPropertyValue('--header-height').replace('rem', ''));
      const yOffset = (headerHeight + 1.5) * parseFloat(getComputedStyle(document.documentElement).fontSize);
      const y = element.getBoundingClientRect().top + window.pageYOffset - yOffset;

      window.scrollTo({top: y, behavior: 'smooth'});
    }
  }

  function addItems(headings, items, level) {
    level++;
    console.log('level', level);

    let index = 0;

    while(index < headings.length) {
      const heading = headings[index];
      heading.id = heading.textContent.toLowerCase().replace(/[^a-zA-Z0-9 ]/g, '').replace(/\s/g, '-');
      const originalElement = heading.innerHTML;
      // const newElement = `<a class="toc-link" href="#${heading.id}">${originalElement}</a>`;
      const newElement = `<a class="toc-link" href="${$url('#' + heading.id)}">${originalElement}</a>`;
      heading.innerHTML = newElement;

      const currentLevel = parseInt(heading.tagName.replace('H', ''), 10);
      const lastHeading = index > 0 ? headings[index - 1] : headings[0];
      const lastLevel = parseInt(lastHeading.tagName.replace('H', ''), 10);
      const nextHeading = index < headings.length - 1 ? headings[index + 1] : null;
      const nextLevel = nextHeading ? parseInt(nextHeading.tagName.replace('H', ''), 10) : -1;

      // [2, [3, 3], 2, [3, 3, 3, 3, 3, 3, 3]]
      // [2, ]

      if (nextLevel === currentLevel) {
        items.push({
          text: heading.textContent,
          link: `${heading.id}`
        });
        index++;
        console.log('level - push item 1', JSON.stringify(items));
      }
      
      if (nextLevel > currentLevel) {
        const children = addItems(headings.slice(index + 1), [], level);
        items.push({
          text: heading.textContent,
          link: `${heading.id}`
        });
        console.log('level - push item 2', JSON.stringify(items));
        const gap = nextLevel - currentLevel;
        items.push(children);
        console.log('level - push items 2', children, JSON.stringify(items));
        console.log('level - index old', index, items.length);
        index = index + children.length + 1;
        console.log('level - index new', index, items.length);
      }
      
      if (nextLevel < currentLevel) {
        console.log('level - push item 3', JSON.stringify(items));
        items.push({
          text: heading.textContent,
          link: `${heading.id}`
        });
        // index++;
        return items;
      }

      console.log('level - index', index, headings.length);
    }

    // headings.forEach((heading, index) => {
    //   // Update heading element with id and anchor tag
    //   heading.id = heading.textContent.toLowerCase().replace(/[^a-zA-Z0-9 ]/g, '').replace(/\s/g, '-');
    //   const originalElement = heading.innerHTML;
    //   const newElement = `<a class="toc-link" href="#${heading.id}">${originalElement}</a>`;
    //   heading.innerHTML = newElement;

    //   const currentLevel = parseInt(heading.tagName.replace('H', ''), 10);
    //   const lastHeading = index > 0 ? headings[index - 1] : headings[0];
    //   const lastLevel = parseInt(lastHeading.tagName.replace('H', ''), 10);
    //   const nextHeading = index < headings.length - 1 ? headings[index + 1] : null;
    //   const nextLevel = nextHeading ? parseInt(nextHeading.tagName.replace('H', ''), 10) : -1;

    //   console.log('level', nextLevel, currentLevel, heading.textContent)

    //   if (nextLevel === currentLevel || index === 0) {
    //     items.push({
    //       text: heading.textContent,
    //       link: `${heading.id}`
    //     });
    //     console.log('level - items push', JSON.stringify(items));
    //   }
      
    //   if (nextLevel > currentLevel) {
    //     console.log('level', headings.slice(index + 1));
    //     items.push(addItems(headings.slice(index + 1), [], level));
    //   } else {
    //     return items;
    //   }
    // });

    // console.log('level - items', items);

    return items;

    // headings.forEach((heading, index) => {
    //   const lastHeading = index > 0 ? headings[index - 1] : headings[0];
    //   const nextHeading = index < headings.length - 1 ? headings[index + 1] : headings[0];
    //   const lastLevel = parseInt(lastHeading.tagName.replace('H', ''), 10);
    //   const nextLevel = parseInt(nextHeading.tagName.replace('H', ''), 10);
    //   const currentLevel = parseInt(heading.tagName.replace('H', ''), 10);

    //   heading.id = heading.textContent.toLowerCase().replace(/[^a-zA-Z0-9 ]/g, '').replace(/\s/g, '-');
    //   const originalElement = heading.innerHTML;
    //   const newElement = `<a class="toc-link" href="#${heading.id}">${originalElement}</a>`;
    //   heading.innerHTML = newElement;

    //   // console.log('level items', items);

    //   console.log('level', heading, currentLevel, lastHeading, lastLevel, JSON.stringify(items));

    //   if (currentLevel > lastLevel) {
    //     console.log('level - 1');
    //     items.push(addItems(headings.slice(index), []));
    //   // } else if (currentLevel < nextLevel) {
    //   } else if (currentLevel < lastLevel) {
    //     console.log('level - 2');
    //     items.push({
    //       text: heading.textContent,
    //       link: `${heading.id}`
    //     });
    //     return items;
    //   } else {
    //     console.log('level - 3');
    //     items.push({
    //       text: heading.textContent,
    //       link: `${heading.id}`
    //     });
    //   }

    //   // console.log('level', headings, heading, currentLevel, lastHeading, lastLevel, items);
    // });

    // // items = [...items];
    // return items;
  }

  function initItems() {
    const headings = document.querySelectorAll('h2, h3, h4, h5, h6');
    console.log('level', headings, Array.prototype.slice.call(headings));

    items = addItems(Array.prototype.slice.call(headings), [], 0);

    // headings.forEach((heading, index) => {
    //   heading.id = heading.textContent.toLowerCase().replace(/[^a-zA-Z0-9 ]/g, '').replace(/\s/g, '-');

    //   const originalElement = heading.innerHTML;
    //   const newElement = `<a class="toc-link" href="#${heading.id}">${originalElement}</a>`;

    //   heading.innerHTML = newElement;

    //   const lastHeading = index > 0 ? headings[index - 1] : headings[0];
    //   const lastLevel = parseInt(lastHeading.tagName.replace('H', ''), 10);
    //   const currentLevel = parseInt(heading.tagName.replace('H', ''), 10);

      

    //   console.log('level', heading, level, lastLevel);

    //   switch (heading.tagName) {
    //     case 'H2':
    //       items.push({
    //         text: heading.textContent,
    //         link: `${heading.id}`
    //       });
    //       break;
    //     case 'H3':
    //       if (!Array.isArray(items[items.length-1])) {
    //         items.push([]);
    //       }
    //       console.log('document.location', document.location);
    //       items[items.length-1].push({
    //         text: heading.textContent,
    //         link: `${heading.id}`
    //       });
    //       break;
    //     // case 'H4':
    //     //   if (!Array.isArray(items[items.length-1][items[items.length-1].length-1])) {
    //     //     items[items.length-1].push([]);
    //     //   }
    //     //   console.log('document.location', document.location);
    //     //   items[items.length-1][items[items.length-1].length-1].push({
    //     //     text: heading.textContent,
    //     //     link: `${heading.id}`
    //     //   });
    //     //   break;
    //   }
    //   // console.log('links', JSON.stringify(links));
    // });

    // items = [...items];

    // const links = document.querySelectorAll('.toc-link');

    // links.forEach((link) => {
    //   link.addEventListener('click', function() {
    //     console.log('link', link, link.href);
    //     const hash = link.href.split('#')[1];
    //     window.event.preventDefault();
        
    //     // if(window.history.pushState) {
    //       window.history.pushState(null, null, '#' + hash);
    //     // } else {
    //     //   window.location.hash = '#' + hash;
    //     // }
    //   }, false);
    // });

    console.log('items', items);
  }
</script>

<style>
  .toc {
    margin: 1.5rem 0 3rem;
  }

  :global(.toc-link) {
    color: var(--text-color);
    position: relative;
    text-decoration: none;
  }

  :global(.toc-link::before) {
    content: "#\00a0";
    color: var(--silver-darken-20);
    position: absolute;
      left: -1em;
  }

  :global(.toc-link:hover::before) {
    color: var(--green-base);
  }
</style>

<div class="toc">
  <TableOfContentsItems {items} />
</div>
