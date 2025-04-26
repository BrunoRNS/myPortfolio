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

# This file is a wrapper for the pyscss library. It compiles scss files to css files in compressed format.
from pathlib import Path
from scss import Compiler

BASE_DIR = Path(__file__).resolve().parent.parent

COMPRESS_DIR = BASE_DIR / 'compressed' / 'app'

def compile_scss(scss_file_content: str) -> str:
   """
   This function compiles a scss string to css in compressed format.
   """
   return str(Compiler().compile_string(string=scss_file_content))