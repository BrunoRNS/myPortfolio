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