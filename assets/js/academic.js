(() => {
  const root = document.documentElement;
  const buttons = document.querySelectorAll('[data-set-theme]');
  const sync = () => buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.setTheme === root.dataset.theme)));
  buttons.forEach(button => button.addEventListener('click', () => {
    root.dataset.theme = button.dataset.setTheme;
    try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
    sync();
  }));
  const media = matchMedia('(prefers-color-scheme: dark)');
  const onChange = event => {
    let saved; try { saved = localStorage.getItem('theme'); } catch (e) {}
    if (saved !== 'light' && saved !== 'dark') { root.dataset.theme = event.matches ? 'dark' : 'light'; sync(); }
  };
  if (media.addEventListener) media.addEventListener('change', onChange);
  sync();

  // Keep third-party JSONP isolated from the homepage and its browser storage.
  const stats = document.querySelector('.visitors');
  if (!stats) return;
  const pv = document.getElementById('busuanzi_value_site_pv');
  const uv = document.getElementById('busuanzi_value_site_uv');
  const retry = document.createElement('button');
  retry.type = 'button';
  retry.textContent = 'Retry';
  retry.hidden = true;
  retry.setAttribute('aria-label', 'Retry loading visitor statistics');
  retry.style.cssText = 'font:inherit;color:inherit;background:transparent;border:1px solid currentColor;border-radius:4px;padding:1px 6px;cursor:pointer';
  stats.appendChild(retry);
  let frame;
  let timer;
  let onCounter;
  let finished = false;
  const cleanup = () => {
    clearTimeout(timer);
    if (onCounter) window.removeEventListener('message', onCounter);
    frame?.remove();
  };
  const unavailable = () => {
    if (finished) return;
    finished = true;
    cleanup();
    pv.textContent = uv.textContent = '—';
    stats.setAttribute('aria-busy', 'false');
    stats.setAttribute('title', 'Visitor statistics could not be loaded. The service or connection may be unavailable; use Retry to try again.');
    retry.hidden = location.hostname !== 'anson-he.github.io';
  };
  const loadCounter = () => {
    cleanup();
    finished = false;
    retry.hidden = true;
    pv.textContent = uv.textContent = '…';
    stats.setAttribute('aria-busy', 'true');
    stats.removeAttribute('title');
    if (location.hostname !== 'anson-he.github.io') { unavailable(); return; }
    frame = document.createElement('iframe');
    frame.src = '/assets/visitor-counter.html?v=20261109-retry';
    frame.setAttribute('sandbox', 'allow-scripts');
    frame.setAttribute('aria-hidden', 'true');
    frame.setAttribute('title', 'Isolated visitor counter');
    frame.tabIndex = -1;
    // Keep it loadable in browsers that defer display:none frames.
    frame.style.cssText = 'position:absolute;width:1px;height:1px;border:0;clip-path:inset(50%);pointer-events:none';
    onCounter = event => {
      if (event.source !== frame.contentWindow || event.origin !== 'null') return;
      const value = event.data;
      if (value?.type === 'site-counter-error-v1') { unavailable(); return; }
      if (value?.type !== 'site-counter-result-v1' ||
          !/^\d{1,20}$/.test(String(value.pv)) || !/^\d{1,20}$/.test(String(value.uv))) return;
      pv.textContent = String(value.pv);
      uv.textContent = String(value.uv);
      stats.setAttribute('aria-busy', 'false');
      stats.removeAttribute('title');
      finished = true;
      cleanup();
    };
    window.addEventListener('message', onCounter);
    frame.onerror = unavailable;
    timer = setTimeout(unavailable, 22000);
    document.body.appendChild(frame);
  };
  retry.addEventListener('click', loadCounter);
  loadCounter();
})();
