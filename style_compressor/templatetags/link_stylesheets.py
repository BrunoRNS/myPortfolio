from style_compressor.templatetags.compress_css import css_file_to_css_string, compress_css
from style_compressor.templatetags.compress_scss import compile_scss_file_to_css_string
from django import template
from pathlib import Path

register = template.Library()

BASE_DIR = Path(__file__).resolve().parent.parent
SCSS_DIR = BASE_DIR / 'compressed' / 'scss'
CSS_DIR = BASE_DIR / 'compressed' / 'css'
UNITED_DIR = BASE_DIR / 'compressed' / 'united'

if not SCSS_DIR.exists():
    SCSS_DIR.mkdir(parents=True)

if not CSS_DIR.exists():
    CSS_DIR.mkdir(parents=True)

if not UNITED_DIR.exists():
    UNITED_DIR.mkdir(parents=True)

def unite_files(template_name: str, files: list[str]) -> Path:
    """
    This function unites the css and scss files in only one, template_name.css and template_name.scss and return the local of them.\n
    """
    if files[0].endswith('.scss'):
        scss: bool = True
    elif files[0].endswith('.css'): 
        scss: bool = False
    else:
        raise ValueError(f"Unsupported file type in list: {files}")
    
    data: str = ""
    for file in files:
        with open(file, 'r') as file:
            data += file.read()
    
    if scss:
        with open(SCSS_DIR / f"{template_name}.scss", 'w') as file:
            file.write(data)
    else:
        with open(CSS_DIR / f"{template_name}.css", 'w') as file:
            file.write(data)
    
    return SCSS_DIR / f"{template_name}.scss" if scss else CSS_DIR / f"{template_name}.css"

@register.simple_tag
def load_stylesheets(template_name: str, css_files: list[str], scss_files: list[str]) -> str:
    """
    This function compresses all the css and scss files in the list in only one file for the app.\n
    The first argument of the list is the name of the template which is using the stylesheet files.\n
    The rest of the list receive the relative dir of the stylesheet files.\n
    The files will be searched in the app's static directory and the global one.\n
    """
    css_united_file: Path = unite_files(template_name, scss_files)
    scss_united_file: Path = unite_files(template_name, css_files)

    css_united_string: str = css_file_to_css_string(css_united_file)
    scss_united_string: str = compile_scss_file_to_css_string(scss_united_file)

    stylesheet_united: str = compress_css(css_united_string + "\n" + scss_united_string)

    with open(UNITED_DIR / f"{template_name}.css", 'w') as file:
        file.write(stylesheet_united)
    
    return str(UNITED_DIR / f"{template_name}.css")