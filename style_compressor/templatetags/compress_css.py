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
import csscompressor

def compress_css(css_content: str) -> str:
    """
    This function compresses a CSS string using the csscompressor library.
    """
    return csscompressor.compress(css_content)

def css_file_to_css_string(css_file_loc:Path) -> str:
    """
    This function compresses a css file using the csscompressor library and returns the compressed css in a string.
    """
    css_file_content: str

    with open(css_file_loc, 'r') as css_file:
        css_file_content = css_file.read()

    return css_file_content