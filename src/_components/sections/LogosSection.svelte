<script>
  import Logos from '../Logos.svelte';

  let communityLogos = [
    {
      title: 'Forum',
      url: 'https://forum.nymea.io/',
      iconSrc: '/img/community/community-discourse-bw.svg'
    },
    {
      title: 'Telegram',
      url: 'https://t.me/nymeacommunity',
      iconSrc: '/img/community/community-telegram.svg'
    },
    {
      title: 'Github',
      url: 'https://github.com/nymea',
      iconName: 'logo-github'
    },
  ];
</script>

<style>
  .community {
    background: linear-gradient(135deg, var(--grey-darken-30), var(--grey-darken-40));
    border-bottom: 1px solid var(--grey-darken-40);
    border-top: 1px solid var(--grey-darken-40);
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
  }
</style>

<section class="community">
  <Logos title="Join our community!" logos={communityLogos} />
</section>
