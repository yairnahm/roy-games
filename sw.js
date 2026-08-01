const CACHE_NAME = 'roy-games-v125';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './images/roys_store_bg.jpg',
  './images/freeze/teddy_dancing.png',
  './images/freeze/teddy_frozen.png',
  './images/gen_missing_r1.png',
  './images/gen_team_r1.png',
  './images/gen_unexpected_r1.png',
  './images/gen_inquiry_r1.png',
  './images/gen_better_r1.png',
  './images/gen_flexibility_r1.png',
  './images/gen_patterns_r1.png',
  './images/gen_decisions_r1.png',
  './images/gen_iteration_r1.png',
  './images/gen_coaching_r1.png',
  './audio/soundmatch/bell.mp3',
  './audio/soundmatch/drum.wav',
  './audio/soundmatch/horn.mp3',
  './audio/soundmatch/car.mp3',
  './audio/soundmatch/phone.mp3',
  './audio/soundmatch/clock.mp3',
  './audio/freeze/dance.mp3',
  './audio/coop/coop_rule_roy.mp3',
  './audio/coop/coop_rule_aba.mp3',
  './audio/coop/coop_memory_praise_roy.mp3',
  './audio/coop/coop_memory_praise_aba.mp3',
  './audio/coop/coop_ask_click.mp3',
  './audio/coop/coop_turn_roy.mp3',
  './audio/coop/coop_turn_aba.mp3',
  './audio/coop/coop_roy_win.mp3',
  './audio/coop/coop_aba_win.mp3',
  './audio/coop/coop_puzzle_victory.mp3',
  './audio/coop/coop_puzzle_err.mp3',
  './audio/coop/tidy_victory.mp3',
  './audio/coop/numwar_roy_win.mp3',
  './audio/coop/numwar_aba_win.mp3',
  './audio/coop/numwar_tie.mp3',
  './audio/coop/numwar_turn_roy.mp3',
  './audio/coop/numwar_turn_aba.mp3',
  './audio/coop/towertalk_turn_roy.mp3',
  './audio/coop/towertalk_turn_aba.mp3',
  './audio/coop/towertalk_err_roy.mp3',
  './audio/coop/towertalk_err_aba.mp3',
  './audio/coop/towertalk_fall.mp3',
  './audio/coop/towertalk_victory.mp3',
  './images/winners/key_roy_reach.png',
  './images/winners/key_grandpa.webp',
  './images/winners/key_teacher.webp',
  './images/winners/key_aba_help.webp',
  './images/roy_hoodie.jpg',
  './images/maor.jpg',
  './images/nitai.jpg',
  './images/aba_yair_sunglasses.jpg',
  './images/saba.jpg',
  './images/adi.jpg',
  './images/alin.jpg',
  './images/arya.jpg',
  './images/yahel.jpg',
  './images/yahli.jpg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS_TO_CACHE))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) =>
      Promise.all(cacheNames.map((cache) => {
        if (cache !== CACHE_NAME) return caches.delete(cache);
      }))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  const url = new URL(event.request.url);

  // Bypass SW for videos (range requests)
  if (url.pathname.endsWith('.mp4') || url.pathname.includes('/videos/')) return;

  // Network-first for HTML — always get the freshest version
  if (event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/')) {
    event.respondWith(
      fetch(event.request).then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const clone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return networkResponse;
      }).catch(() => caches.match(event.request))
    );
    return;
  }

  // Cache-first for all other assets (images, audio, fonts)
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) return cachedResponse;
      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200) return networkResponse;
        const clone = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        return networkResponse;
      }).catch(() => {});
    })
  );
});
