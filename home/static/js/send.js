/* 
Project: server - My Portfolio
Author: Bruno Rian Nunes de Souza
License: GNU General Public License v3.0

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License, version 3, as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
*/

/**
 * Handles the form submission and sends a POST request to the Django view.
 *
 * @param {Event} e The submit event
*/
document
.getElementById('contactForm')
.addEventListener('submit', async function (e) {
    e.preventDefault();

    const form = e.target;
    const submitBtn = document.getElementById('submitBtn');
    const formData = new FormData(form);

    submitBtn.disabled = true;

    try {
        const response = await fetch('/send/', {
            method: 'POST',
            body: formData,
            credentials: 'same-origin',
            headers: {
                'X-CSRFToken': form.querySelector(
                    '[name=csrfmiddlewaretoken]'
                ).value
            }
        });

        if (response.status === 403) {
            throw new Error(
                'Your request was blocked. Please refresh the page and try again.'
            );
        }

        if (!response.ok) {
            throw new Error(
                'An internal error occurred. Please try again later.'
            );
        }

        alert('Message sent successfully!');
        form.reset();

    } catch (err) {
        alert(err || 'Unexpected error occurred, please send an issue to the github repository.');
    } finally {
        submitBtn.disabled = false;
    }
});

/*
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    form.reset();
});
*/

(function securityLayer() {
    const CONFIG = {
        minClickInterval: 800,
        minTimeOnPage: 3000,
        elementCooldown: 5000
    };

    const loadedAt = Date.now();
    let lastGlobalClick = 0;
    const lastElementAction = new WeakMap();

    document.addEventListener('click', function (e) {
        const now = Date.now();

        if (now - lastGlobalClick < CONFIG.minClickInterval) {
            e.preventDefault();
            e.stopPropagation();
            return;
        }
        lastGlobalClick = now;
        const el = e.target.closest('button, a, input[type=submit]');
        if (!el) return;

        const last = lastElementAction.get(el) || 0;
        if (now - last < CONFIG.elementCooldown) {
            e.preventDefault();
            e.stopPropagation();
            return;
        }

        lastElementAction.set(el, now);
    }, true);

    document.addEventListener('submit', function (e) {
        const now = Date.now();
        
        if (now - loadedAt < CONFIG.minTimeOnPage) {
            e.preventDefault();
            return;
        }

        let honeypot = e.target.querySelector('input[name="_session"]');
        if (!honeypot) {
            honeypot = document.createElement('input');
            honeypot.type = 'text';
            honeypot.name = '_session';
            honeypot.autocomplete = 'off';
            honeypot.tabIndex = -1;
            honeypot.style.display = 'none';
            e.target.appendChild(honeypot);
        }

        if (honeypot.value) {
            e.preventDefault();
            return;
        }
    }, true);
})();

