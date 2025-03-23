from compress_scss import _compress_scss
from compress_css import _compress_css
from django import template

register = template.Library()

@register.filter
def main(files: list[str]) -> str:
    """
    This function compresses all the css and scss files in the list in only one file for the app.\n
    The first argument is the name of the app and of the template, in this format: "appName__templateName".\n
    The rest of the list receive the relative dir of the stylesheet files.\n
    The files will be searched in the app's static directory and the global one.\n
    """
