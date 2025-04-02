# This file is a wrapper for the libsass library. It compiles scss files to css files in compressed format.
from pathlib import Path
import sass

BASE_DIR = Path(__file__).resolve().parent.parent

COMPRESS_DIR = BASE_DIR / 'compressed' / 'app'

def compile_scss(scss_file_content: str) -> str:
   """
   This function compiles a scss string to css in compressed format.
   """
   return sass.compile(string=scss_file_content, output_style='compressed')
