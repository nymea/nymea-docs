/* A finite, seekable Hyperframes timeline. The player owns playback. */
(() => {
  const timeline = gsap.timeline({ paused: true });
  document.querySelectorAll('[data-flow]').forEach((path, index) => {
    const length = path.getTotalLength();
    const electricity = path.dataset.flow === 'power';
    const count = electricity ? 4 : 3;
    const dash = electricity ? Math.min(17, length / count * 0.3) : 3;
    const phase = (index % 3) * length / 9;
    path.setAttribute('stroke-dasharray', `${dash} ${length / count - dash}`);
    timeline.fromTo(path,
      { attr: { 'stroke-dashoffset': phase } },
      { attr: { 'stroke-dashoffset': phase - length }, duration: 12, ease: 'none' }, 0);
  });
  timeline.fromTo('#hub-halo', { opacity: 0.2 },
    { opacity: 0.65, duration: 1.5, repeat: 7, yoyo: true, ease: 'sine.inOut' }, 0);
  ['#bar-1', '#bar-2', '#bar-3'].forEach((bar, index) => {
    const startHeight = [15, 22, 17][index];
    const endHeight = [9, 16, 10][index];
    timeline.fromTo(bar, { attr: { y: 46 - startHeight, height: startHeight } },
      { attr: { y: 46 - endHeight, height: endHeight }, duration: 3, repeat: 3,
        yoyo: true, ease: 'sine.inOut' }, 0);
  });
  window.__timelines = window.__timelines || {};
  window.__timelines['energy-flow'] = timeline;
})();
