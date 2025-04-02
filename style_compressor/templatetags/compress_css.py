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