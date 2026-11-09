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

  // Use Vercount's JSON API; no third-party script executes in this page.
  const stats = document.querySelector('.visitors');
  if (!stats) return;
  const pv = document.getElementById('busuanzi_value_site_pv');
  const uv = document.getElementById('busuanzi_value_site_uv');
  const unavailable = () => {
    pv.textContent = uv.textContent = '—';
    stats.setAttribute('aria-busy', 'false');
    stats.setAttribute('title', 'Visitor statistics are temporarily unavailable.');
  };
  if (location.hostname !== 'anson-he.github.io') { unavailable(); return; }
  const cookieName = 'vercount_uv_' + location.host.replace(/[^a-zA-Z0-9_-]/g, '_');
  let isNewUv = true;
  try {
    isNewUv = !document.cookie.split(';').some(value => value.trim() === cookieName + '=1');
  } catch (e) {}
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 10000);
  const loadCounter = async () => {
    try {
      const response = await fetch('https://events.vercount.one/api/v2/log', {
        method: 'POST',
        credentials: 'omit',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url: location.origin + location.pathname, isNewUv }),
        signal: controller.signal
      });
      if (!response.ok) throw new Error('Counter request failed');
      const result = await response.json();
      const counts = result.data;
      if (result.status !== 'success' || !counts ||
          !/^\d{1,20}$/.test(String(counts.site_pv)) ||
          !/^\d{1,20}$/.test(String(counts.site_uv))) throw new Error('Invalid counter response');
      pv.textContent = String(counts.site_pv);
      uv.textContent = String(counts.site_uv);
      stats.setAttribute('aria-busy', 'false');
      stats.removeAttribute('title');
      // Match the provider's first-party UV cookie, only after a successful count.
      if (isNewUv) {
        try { document.cookie = cookieName + '=1; path=/; max-age=31536000; samesite=lax; secure'; } catch (e) {}
      }
    } catch (e) {
      unavailable();
    } finally {
      clearTimeout(timeout);
    }
  };
  loadCounter();
})();
