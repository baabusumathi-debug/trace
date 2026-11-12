// Trace service worker: keeps the whole app on the device so it opens with no internet.
// Card data lives in IndexedDB (not here). Bump VERSION on every release.
// the test build (/trace/test/) keeps caches under its own prefix so the two never clear each other
const PREFIX = self.registration.scope.includes('/test/') ? 'tracetest-v' : 'trace-v';
const VERSION = PREFIX + '1.3.119';
const SHELL = [
  './', 'index.html', 'manifest.webmanifest', 'css/app.css',
  'js/app.js', 'js/api.js', 'js/config.js', 'js/db.js', 'js/emblems.js', 'js/md.js', 'js/store.js', 'js/viva.js', 'js/voice.js', 'js/lesson.js', 'js/sync.js', 'js/palace.js', 'js/visuals.js', 'js/flowmsg.js', 'js/loftx.js', 'js/breaks.js', 'js/peek.js', 'js/peakdata.js', 'js/plan.js', 'js/day.js', 'js/desk.js', 'js/ink.js', 'js/inkcard.js', 'js/explain.js', 'img/palace-land.webp', 'img/palace-port.webp',
  'icons/icon.svg', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png',
  'fonts/cormorant-garamond-latin-500-normal.woff2', 'fonts/cormorant-garamond-latin-600-normal.woff2', 'fonts/cormorant-garamond-latin-700-normal.woff2',
  'fonts/inter-latin-400-normal.woff2', 'fonts/inter-latin-400-italic.woff2', 'fonts/inter-latin-500-normal.woff2', 'fonts/inter-latin-600-normal.woff2', 'fonts/inter-latin-700-normal.woff2',
  'fonts/ibm-plex-mono-latin-400-normal.woff2', 'fonts/ibm-plex-mono-latin-500-normal.woff2'
];

self.addEventListener('install', e => {
  // take over as soon as the new files are cached; the page reloads itself unless a flow is running
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(SHELL.map(u => new Request(u, { cache: 'reload' })))).then(() => self.skipWaiting()));
});
self.addEventListener('message', e => { if (e.data === 'skip') self.skipWaiting(); });
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith(PREFIX) && k !== VERSION) await caches.delete(k);
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;   // backend calls go straight to the network
  if (url.pathname.endsWith('/data/qbank.json') || url.pathname.endsWith('/data/qmap.json') || url.pathname.endsWith('/data/cardfix.json') || /\/data\/viva\/[^/]+\.json$/.test(url.pathname)) return;                       // QBank layer: always fresh; the app keeps its own offline copy
  e.respondWith((async () => {
    const cache = await caches.open(VERSION);
    const hit = await cache.match(e.request, { ignoreSearch: url.pathname.endsWith('/') || url.pathname.endsWith('index.html') });
    if (hit) return hit;
    try {
      const res = await fetch(e.request);
      if (res.ok) cache.put(e.request, res.clone());          // self-heal: anything missing is kept for next time offline
      return res;
    } catch (err) {
      if (e.request.mode === 'navigate') return (await cache.match('index.html')) || Response.error();
      return Response.error();
    }
  })());
});
