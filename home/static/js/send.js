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
document.getElementById('contactForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitBtn = document.getElementById('submitBtn');
    const formData = new FormData(form);
    
    submitBtn.disabled = true;
    
    try {

        const response = await fetch('/send/', {

            method: 'POST',
            body: formData,

            headers: {
                'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
            }

        });
        
        const data = await response.json();
        
        if (!response.ok) {

            throw new Error(data.errors || 'Failed to send');

        }
        
        alert('Message sent successfully!');
        form.reset();

    } catch (error) {

        alert('Error: ' + (error.message || 'Please try again later'));

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