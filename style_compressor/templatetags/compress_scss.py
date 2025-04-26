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

from style_compressor.templatetags.pyscss_wrapper import compile_scss
from pathlib import Path

def compile_scss_file_to_css_string(scss_file: Path) -> str:
    """
    This function compiles a SCSS file into CSS using the libsass library.
    """
    with open(scss_file, 'r') as file:
        scss_file_content = file.read()

    return compile_scss(scss_file_content)