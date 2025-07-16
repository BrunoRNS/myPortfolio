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

from pathlib import Path
import re

pathToIndex = Path(__file__).parent.parent / "templates" / "index.html"

with open(pathToIndex, 'r', encoding='utf-8') as file:
    content = file.read()

content = re.sub(r'/static/(.+?)"', r"{% static '\1' %}\"", content)
content = content.replace('/favicon.png', '{% static \'favicon.png\' %}')

with open(pathToIndex, 'w', encoding='utf-8') as file:
    file.write(content)
