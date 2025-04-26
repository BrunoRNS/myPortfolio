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

from style_compressor.templatetags.compress_css import css_file_to_css_string, compress_css
from style_compressor.templatetags.compress_scss import compile_scss_file_to_css_string

from style_compressor.templatetags.link_stylesheets_exceptions import MissedscssException, \
MissedcssException, MissedtemplateException, NotdictException, NotlistException, NotstrException

from server.settings import STATICFILES_DIRS, BASE_DIR, MY_APPS

from django import template
from pathlib import Path

register = template.Library()

SCSS_DIR = BASE_DIR / 'compressed' / 'scss'
CSS_DIR = BASE_DIR / 'compressed' / 'css'
UNITED_DIR = BASE_DIR / 'compressed' / 'united'

class Validater(object):
    """
    This class validate the context received in the template.\n

    - It checks if the keys are strings and the values are lists.\n
    - It checks if the css_files, scss_files and template_name keys are not empty.\n
    - It checks if the template name is a string.\n
    - It checks if the css and scss files exist.\n
    - It creates the directories for the compressed files.\n
    """

    def __init__(self, stylesheet: dict[str: list[str]]) -> tuple[list[str], list[str], list[str]]:
        """
        __init__ method of the Validater class.\n
        It receives a dictionary with the keys 'css_files', 'scss_files' and 'template_name' from the context.\n
        """

        self.create_dirs()
        
        self.stylesheet = stylesheet

        self.validate_stylesheet_typing()

        self.css_files: list[str] = stylesheet.get('css_files', [])
        self.scss_files: list[str] = stylesheet.get('scss_files', [])
        self.template_name: list[str] = stylesheet.get('template_name', [])

        self.check_not_empty()
        self.check_template_name()
        self.check_files_exist()

        # Returns the css_files, scss_files and template_name keys if everything executed successufully.

        return (self.css_files, self.scss_files, self.template_name)

    @staticmethod
    def create_dirs() -> None:
        """
        This function creates the directories for the compressed files.\n
        """
        if not SCSS_DIR.exists():
            SCSS_DIR.mkdir(parents=True)

        if not CSS_DIR.exists():
            CSS_DIR.mkdir(parents=True)

        if not UNITED_DIR.exists():
            UNITED_DIR.mkdir(parents=True)


    def validate_stylesheet_typing(self) -> None:
        """
        This function validates the types of the stylesheet dictionary.\n
        It checks if the keys are strings and the values are lists.\n
        """
        if not isinstance(self.stylesheet, dict):
            raise NotdictException(
                message = "The stylesheet parameter must be a dictionary.",
                description = "Expected: dict[str: list[str]]\n" 
                    + "Got: " + str(type(self.stylesheet)) + "\n" 
                    + "Value: " + str(self.stylesheet) + "\n",
            )

        if not all(isinstance(value, list) for value in self.stylesheet.values()):
            raise NotlistException(
                message = "All values in the stylesheet dictionary must be lists.",
                description = str(
                    *("Type: " + str(type(value)) + " of element " + str(value) + " in stylesheet\n"
                    for value in self.stylesheet.values() if not isinstance(value, list))
                ),
            )
    
    def check_not_empty(self) -> None:
        """
        This function checks if the css_files, scss_files and template_name keys are not empty.\n
        """
        if not self.css_files:
            raise MissedcssException(
                message = "No CSS files provided in the stylesheet dictionary.",
                description = str(self.stylesheet),
            )
    
        if not self.scss_files:
            raise MissedscssException(
                message = "No SCSS files provided in the stylesheet dictionary.",
                description = str(self.stylesheet),
            )
    

        if not self.template_name:
            raise MissedtemplateException(
                message = "No template name provided in the stylesheet dictionary.",
                description = str(self.stylesheet) + "\n" + \
                    type(self.stylesheet['template_name'] \
                    if 'template_name' in list(self.stylesheet.keys()) \
                    else "No template name provided in the stylesheet dictionary." \
                ),
            )
    
    def check_template_name(self) -> None:
        """
        This function checks if the template name is a string.\n
        """
        if not isinstance(self.template_name[0], str):
            raise NotstrException(
                message = "The template name must be a string.",
                description = str(self.template_name[0]) + "\n" \
                    + "Type: " + str(type(self.template_name[0])) + "\n",
            )
    
    def check_files_exist(self) -> None:
        """
        This function checks if the css and scss files exist.\n
        """
        for file in self.css_files + self.scss_files:
            if not (BASE_DIR / file).exists():
                raise FileNotFoundError(
                    message = "File not found: " + str(file),
                    description = str(file) + "\n" + "Type: " + str(type(file)) + "\n",
                )

class StaticDirsCollector(object):
    # Returns the static files directories to the variable which will initialize the class.\n

    def __init__(self, STATICFILES_DIRS: list[Path], MY_APPS: list[str]) -> list[Path]:
        """
        This class receives a list of paths to the static files directories from django settings.\n
        And a list of the apps of the django server.\n
        It adds to an empty list the static files directories 
        from the settings and from the apps of the server.\n
        It returns a list of paths to the static files directories.\n
        """
        self.static_files_dirs = []

        self.static_files_dirs = self.add_static_dirs_from_settings(STATICFILES_DIRS)

        self.static_files_dirs = self.add_static_dirs_from_apps(self.static_files_dirs, MY_APPS)

        return self.static_files_dirs

    @staticmethod
    def add_static_dirs_from_settings(static_files_list: list, STATICFILES_DIRS: list[Path]) -> None:
        """
        This function adds the static directory to the list of static directories.\n
        """
        static_files_list.append(STATICFILES_DIRS)
        return static_files_list
    
    @staticmethod
    def add_static_dirs_from_apps(static_files_list: list, MY_APPS: list[str]) -> None:
        """
        This function adds the static directory to the list of static directories.\n
        """
        
        return static_files_list.append(
            BASE_DIR / MY_APP / 'static' \
            
            for MY_APP in MY_APPS \
                if MY_APP != 'style_compressor' and (BASE_DIR / MY_APP / 'static').exists() \
        )

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
def load_stylesheets(stylesheet: dict[str: list[str]]) -> str:
    """
    This function compresses all the css and scss files in the list in only one file for the app.\n
    It receives a dictionary with the keys 'css_files', 'scss_files' and 'template_name'.\n
    The values of the keys are lists of strings with the paths of the files.\n
    The paths of the files are relative to the app's static directory.\n
    The files will be searched in the app's static directory and the global one.\n
    """
    
    # Typing the stylesheet dict elements
    css_files: list[str]
    scss_files: list[str]
    template_name: list[str]

    # Validate the stylesheet dictionary
    css_files, scss_files, template_name = Validater(stylesheet)

    css_united_file: Path = unite_files(template_name[0], scss_files)
    scss_united_file: Path = unite_files(template_name[0], css_files)

    css_united_string: str = css_file_to_css_string(css_united_file)
    scss_united_string: str = compile_scss_file_to_css_string(scss_united_file)

    stylesheet_united: str = compress_css(css_united_string + "\n" + scss_united_string)

    with open(UNITED_DIR / f"{template_name[0]}.css", 'w') as file:
        file.write(stylesheet_united)
    
    return str(UNITED_DIR / f"{template_name[0]}.css")