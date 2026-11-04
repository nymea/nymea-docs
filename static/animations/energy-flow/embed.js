(() => {
  const player = document.querySelector('#player');
  const button = document.querySelector('#play');
  const state = document.querySelector('#state');
  const theme = document.querySelector('#theme');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const dark = matchMedia('(prefers-color-scheme: dark)');
  let wantsPlayback = !reduced.matches;
  let inView = true;
  let hostRoot;
  try { hostRoot = window.parent.document.documentElement; } catch { /* Cross-origin embeds follow the OS. */ }
  const requested = new URLSearchParams(location.search).get('theme');
  if (['light', 'dark'].includes(requested)) theme.value = requested;

  function syncTheme() {
    const hostTheme = hostRoot !== document.documentElement ? hostRoot?.dataset.theme : null;
    const resolved = theme.value === 'auto'
      ? (['light', 'dark'].includes(hostTheme) ? hostTheme : dark.matches ? 'dark' : 'light')
      : theme.value;
    document.documentElement.dataset.theme = resolved;
    const inner = player.iframeElement?.contentDocument;
    if (inner) inner.documentElement.dataset.theme = resolved;
  }

  function syncPlayback() {
    if (!player.ready) return;
    if (wantsPlayback && inView && !document.hidden) player.play();
    else player.pause();
    button.textContent = wantsPlayback ? 'Pause animation' : 'Play animation';
    state.textContent = wantsPlayback ? 'Live flow illustration' : reduced.matches ? 'Reduced motion · paused' : 'Animation paused';
  }

  player.addEventListener('ready', () => {
    syncTheme();
    document.querySelector('main').classList.add('ready');
    button.disabled = false;
    syncPlayback();
  });
  player.addEventListener('error', () => {
    document.querySelector('main').classList.remove('ready');
    button.disabled = true;
    state.textContent = 'Static energy flow diagram';
  });
  // Handle clicks inside the player as well as the accessible external button.
  player.setAttribute('disable-click-to-play', '');
  button.addEventListener('click', () => { wantsPlayback = !wantsPlayback; syncPlayback(); });
  theme.addEventListener('change', syncTheme);
  dark.addEventListener('change', syncTheme);
  reduced.addEventListener('change', () => { wantsPlayback = !reduced.matches; syncPlayback(); });
  document.addEventListener('visibilitychange', syncPlayback);
  new IntersectionObserver(([entry]) => { inView = entry.isIntersecting; syncPlayback(); }).observe(player);
  if (hostRoot && hostRoot !== document.documentElement) {
    new MutationObserver(syncTheme).observe(hostRoot, { attributes: true, attributeFilter: ['data-theme'] });
  }
  syncTheme();
})();
