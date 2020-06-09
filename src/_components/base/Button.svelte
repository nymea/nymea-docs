<script>
  export let text = 'Button';
  export let link = '#';
</script>

<style>
  .button {
    background-color: var(--grey-darken-40);
    color: var(--silver-base);
    border-radius: 5px;
    display: inline-block;
    padding: var(--space-04) var(--space-07);
    text-decoration: none;
  }

  .button :global(ion-icon) {
    font-size: 1.125rem;
    transform: translateY(0.15em);
    transition: transform 100ms ease-in-out;
  }

  .button :global(slot[name="start"] ion-icon) {
    transform: translateX(-0.375rem);
  }

  .button:hover :global(slot[name="start"] ion-icon) {
    transform: translateX(-0.5rem) translateY(0.15em);
  }

  .button :global(slot[name="end"] ion-icon) {
    transform: translateX(0.375rem);
  }

  .button:hover :global(slot[name="end"] ion-icon) {
    transform: translateX(0.5rem) translateY(0.15em);
  }
</style>

<a href={link} class="button">
  <slot name="start" />
  {text}
  <slot name="end" />
</a>
