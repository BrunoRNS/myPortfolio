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
 * Toggle the visibility of the Beecrowd image and separator.
 * If the viewport's width is less than or equal to 767px, the image and separator are hidden.
 * Otherwise, they are shown.
*/
function toggleBeeImgVisibility() {

    const beeImg = document.querySelector('.bee-img');
    const beeSeparator = document.querySelector('.bee-separator');

    if (window.matchMedia("(max-width: 815px)").matches) {

        beeImg.style.display = 'none';
        beeSeparator.style.display = 'none';

    } else {

        beeImg.style.display = 'block';
        beeSeparator.style.display = 'block';

    }
}

window.addEventListener('DOMContentLoaded', toggleBeeImgVisibility);

window.addEventListener('resize', toggleBeeImgVisibility);
