'use strict';

const CACHE_NAME = 'static-cache';
const FILES_TO_CACHE = [
  '/project/static/offline.html',
];

// Installation
self.addEventListener('install', (e) => {
  console.log('[ServiceWorker] Install');
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[Service Worker] Pre-caching offline page.');
      return cache.addAll(FILES_TO_CACHE);
    }).catch(err => console.log(err))
  );
  self.skipWaiting();
});

// Activation
self.addEventListener('activate', (e) => {
  console.log('[ServiceWorker] Activate', caches);
  e.waitUntil(
    caches.keys().then((keyList) => {
        return Promise.all(keyList.map((key) => {
          if (key !== CACHE_NAME) {
            console.log('[Service Worker] Removing old cache', key);
            return cache.delete(key);
          }
        }));
      })
  );
  self.clients.claim();
});

// Fetch
self.addEventListener('fetch', (e) => {
  e.respondWith(
    fetch(e.request).catch(() => {
      return caches.match(e.request); // network falling back to cache
    })
  );
});

// Push Notifications
self.addEventListener('push', (e) => {
  console.log('[Service Worker] Push Received.');
  const title = 'Flask PWA';
  const options = {
    body: e.data.text(),
    icon: 'static/images/favicon-32x32.png',
    vibrate: [50, 50, 50],
    sound: 'static/audio/notification-sound.mp3'
  };
  e.waitUntil(self.registration.showNotification(title, options));
})
