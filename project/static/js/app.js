'use strict';

// Registration
if ('serviceWorker' in navigator) {
  navigator.serviceWorker
  .register('./sw.js')
  .then((registration) => {
    console.log('Service Worker Registered!');
    return registration;
  })
  .catch((err) => {
    console.error('Unable to register service worker.', err);
  });
}

// Push Notifications
const pushButton = document.getElementById('pushButton');
if (!("Notification" in window)) {
  pushButton.setAttribute('hidden', true);
}
pushButton.addEventListener('click', (e) => {
  e.srcElement.setAttribute('hidden', true);
  Notification.requestPermission().then((permission) => {
    notificationButtonUpdate();
  });
});
notificationButtonUpdate();

function notificationButtonUpdate() {
  if (Notification.permission == 'granted') {
    pushButton.setAttribute('hidden', true);
  } else {
    pushButton.removeAttribute('hidden');
  }
}

// Geolocation
if ('geolocation' in navigator) {
  document.getElementById('askLocation')
  .addEventListener('click', () => {
    navigator.geolocation.getCurrentPosition((position) => {
      console.log(position);
    });
  });
} else {
  console.log('Geolocation API not supported.');
}
