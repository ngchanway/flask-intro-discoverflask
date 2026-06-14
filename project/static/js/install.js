'use strict';

// Install Button
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault();
  deferredPrompt = e;
  if (installButton) {
    installButton.removeAttribute('hidden');
  }
});

const installButton = document.getElementById('installButton');
if (installButton) {
  installButton.addEventListener('click', (e) => {
    console.log(deferredPrompt);//
    deferredPrompt.prompt();
    e.srcElement.setAttribute('hidden', true);
    deferredInstallPrompt.userChoice.then((choice) => {
      if (choice.outcome === 'accepted') {
        console.log('User accepted the A2HS prompt', choice);
      } else {
        console.log('User dismissed the A2HS prompt', choice);
      }
      deferredInstallPrompt = null;
    });
  });
}

window.addEventListener('appinstalled', (e) => {
  console.log('App was installed.', e);
})
