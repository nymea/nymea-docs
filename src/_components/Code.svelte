<script>
  import { onMount } from 'svelte';
  import { Tabs, TabPane } from './tabs/_tabs.js';

  let code;
  let tabPanes = [];

  onMount(() => {
    const codeBlocks = code.querySelectorAll('.code');

    let className;
    let languageList;
    let language;

    codeBlocks.forEach((codeBlock) => {
      className = codeBlock.querySelector('code').className;
      languageList = className.match(/language-.* /);
      language = languageList ? languageList[0].replace('language-', '') : '';

      tabPanes.push({
        codeBlock: `<pre>${codeBlock.innerHTML}</pre>`,
        name: language
      });
    });

    tabPanes = [ ...tabPanes ];
  });
</script>

<style>
  .code {
    display: flex;
  }

  .code > :global(.code) {
    display: none;
  }
</style>

<div bind:this={code} class="code">
  <Tabs>
    {#each tabPanes as tabPane}
      <TabPane name={tabPane.name}>
        {@html tabPane.codeBlock}
      </TabPane>
    {/each}
  </Tabs>
  <slot />
</div>
