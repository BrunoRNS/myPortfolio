""" 
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
"""

from django.shortcuts import render

# Home Page
def home(request):

    stylesheet: dict[str: list[str]] = {
        'css_files': ["home/home/col_img.css", "home/home/col_portfolio.css"],
        'scss_files': ["global/global.scss", "home/home/page.scss"],
        'template_name': ["home"],
    }
    
    return render(request, 'home/home/index.html', context=stylesheet)