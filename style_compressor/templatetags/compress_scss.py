from style_compressor.templatetags.pyscss_wrapper import compile_scss
from pathlib import Path

def compile_scss_file_to_css_string(scss_file: Path) -> str:
    """
    This function compiles a SCSS file into CSS using the libsass library.
    """
    with open(scss_file, 'r') as file:
        scss_file_content = file.read()

    return compile_scss(scss_file_content)