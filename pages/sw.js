// Study pages: network first, so an updated page arrives on its own; the cache is the offline copy.
const V = 'pages-v3';
const FILES = ['./', 'index.html', 'shock1.html', 'gi.html', 'endo.html', 'obs.html',
               'manifest.webmanifest', 'shock1.webmanifest', 'gi.webmanifest', 'endo.webmanifest', 'obs.webmanifest',
               'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png',
               'icons/shock1-192.png', 'icons/gi-192.png', 'icons/endo-192.png', 'icons/obs-192.png',
               'icons/shock1-512.png', 'icons/gi-512.png', 'icons/endo-512.png', 'icons/obs-512.png',
               'css/ink.css', 'css/desk.css',
               'js/desk.js', 'js/ink-mount.js', 'js/notes.js', 'js/paper.js', 'js/store.js'];
self.addEventListener('install', e => {
  e.waitUntil(caches.open(V)
    .then(c => Promise.allSettled(FILES.map(u => c.add(new Request(u, { cache: 'reload' })))))
    .then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k.startsWith('pages-') && k !== V) await caches.delete(k);
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  e.respondWith((async () => {
    const cache = await caches.open(V);
    try {
      const res = await fetch(e.request);
      if (res && res.ok) cache.put(e.request, res.clone());
      return res;
    } catch (err) {
      const hit = await cache.match(e.request, { ignoreSearch: true });
      if (hit) return hit;
      if (e.request.mode === 'navigate') {
        const i = await cache.match('index.html');
        if (i) return i;
      }
      return Response.error();
    }
  })());
});
