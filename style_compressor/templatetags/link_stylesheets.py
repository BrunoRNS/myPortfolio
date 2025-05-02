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
MissedcssException, MissedtemplateException, NotdictException, NotlistException, NotstrException, \
ValidationError

from server.settings import STATICFILES_DIRS, BASE_DIR, MY_APPS

from django import template
from pathlib import Path

from typing import Dict, List, Tuple

register = template.Library()

SCSS_DIR = BASE_DIR / 'compressed' / 'scss'
CSS_DIR = BASE_DIR / 'compressed' / 'css'
UNITED_DIR = BASE_DIR / 'compressed' / 'united'

class Validator(object):
    """
    This class validate the context received in the template.\n

    - It checks if the keys are strings and the values are Lists.\n
    - It checks if the css_files, scss_files and template_name keys are not empty.\n
    - It checks if the template name is a string.\n
    - It checks if the css and scss files exist.\n
    - It creates the directories for the compressed files.\n
    """

    stylesheet: Dict[str, List[str]]

    def __init__(self, stylesheet: Dict[str, List[str]]) -> None:
        """
        __init__ method of the Validater class.\n
        It receives a Dictionary with the keys 'css_files', 'scss_files' and 'template_name' from the context.\n
        """

        self.create_dirs()
        
        self.stylesheet = stylesheet

        self.validate_stylesheet_typing()

        self.css_files: List[str] = stylesheet.get('css_files', [])
        self.scss_files: List[str] = stylesheet.get('scss_files', [])
        self.template_name: List[str] = stylesheet.get('template_name', [])

        self.check_not_empty()
        self.check_template_name()

        return None

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
        :param self: The class itself.\n
        :return: None.\n
        :raises NotdictException: If the stylesheet parameter is not a Dictionary.\n
        :raises NotlistException: If the values of the stylesheet Dictionary are not Lists.\n

        This function validates the types of the stylesheet Dictionary.\n
        It checks if the keys are strings and the values are Lists.\n
        """
        if not isinstance(self.stylesheet, dict):
            raise NotdictException(
                message = "The stylesheet parameter must be a Dictionary.",
                description = "Expected: Dict[str: List[str]]\n" 
                    + "Got: " + str(type(self.stylesheet)) + "\n" 
                    + "Value: " + str(self.stylesheet) + "\n",
            )

        if not all(isinstance(value, list) for value in self.stylesheet.values()):
            raise NotlistException(
                message = "All values in the stylesheet Dictionary must be Lists.",
                description = str(
                    *("Type: " + str(type(value)) + " of element " + str(value) + " in stylesheet\n"
                    for value in self.stylesheet.values() if not isinstance(value, list))
                ),
            )
    
    def check_not_empty(self) -> None:
        """
        :param self: The class itself.\n
        :return: None.\n
        :raises MissedcssException: If the css_files key is empty.\n
        :raises MissedscssException: If the scss_files key is empty.\n
        :raises MissedtemplateException: If the template_name key is empty.\n

        This function checks if the css_files, scss_files and template_name keys are not empty.\n
        """
        if not self.css_files:
            raise MissedcssException(
                message = "No CSS files provided in the stylesheet Dictionary.",
                description = str(self.stylesheet),
            )
    
        if not self.scss_files:
            raise MissedscssException(
                message = "No SCSS files provided in the stylesheet Dictionary.",
                description = str(self.stylesheet),
            )
    

        if not self.template_name:
            raise MissedtemplateException(
                message = "No template name provided in the stylesheet Dictionary.",
                description = str((self.stylesheet) + "\n" + \
                    type(self.stylesheet['template_name']) \
                    if "template_name" in list(self.stylesheet.keys()) \
                    else "No template name provided in the stylesheet Dictionary." \
                ),
            )
    
    def check_template_name(self) -> None:
        """
        :param self: The class itself.\n
        :return: None.\n
        :raises NotstrException: If the template name is not a string.\n

        This function checks if the template name is a string.\n
        """
        if not isinstance(self.template_name[0], str):
            raise NotstrException(
                message = "The template name must be a string.",
                description = str(self.template_name[0]) + "\n" \
                    + "Type: " + str(type(self.template_name[0])) + "\n",
            )
    
    @staticmethod
    def check_files_exist(files: List[Path]) -> None:
        """
        This function checks if the css and scss files exist.\n
        """
        for file in files:
            if not (BASE_DIR / file).exists():
                raise FileNotFoundError(
                    "File not found: " + str(file)
                )
    
    def return_if_ok(self) -> Tuple[List[str], List[str], List[str]]:
        """
        :param cls: The class itself.\n
        :return: A tuple with the css_files, scss_files and template_name keys.\n

        This function returns the css_files, scss_files and template_name keys if everything executed successufully.\n
        """
        try:
            return self.stylesheet.get('css_files', []), \
                self.stylesheet.get('scss_files', []), \
                self.stylesheet.get('template_name', [])
        
        except Exception as e:
            raise ValidationError(
                message = "Unknown Error in the stylesheet Dictionary.",
                description = str(e),
            )

class StaticDirsCollector(object):
    # Returns the static files directories to the variable which will initialize the class.\n

    def __init__(self, STATICFILES_DIRS: List[Path], MY_APPS: List[str]) -> None:
        """
        This class receives a List of paths to the static files directories from django settings.\n
        And a List of the apps of the django server.\n
        It adds to an empty List the static files directories 
        from the settings and from the apps of the server.\n
        It returns a List of paths to the static files directories.\n
        """
        self.static_files_dirs: List[Path] = []

        self.static_files_dirs = self.add_static_dirs_from_settings(STATICFILES_DIRS)

        self.static_files_dirs = self.add_static_dirs_from_apps(self.static_files_dirs, MY_APPS)


    @staticmethod
    def add_static_dirs_from_settings(STATICFILES_DIRS: List[Path]) -> None:
        """
        This function adds the static directory to the List of static directories.\n
        """
        static_files_List: List[Path] = []
        static_files_List.append(STATICFILES_DIRS)
        return static_files_List
    
    @staticmethod
    def add_static_dirs_from_apps(static_files_List: List, MY_APPS: List[str]) -> None:
        """
        This function adds the static directory to the List of static directories.\n
        """
        
        return static_files_List.append(
            BASE_DIR / MY_APP / 'static' \
            
            for MY_APP in MY_APPS \
                if MY_APP != 'style_compressor' and (BASE_DIR / MY_APP / 'static').exists() \
        )
    
    def return_static_dirs(self) -> List[Path]:
        """
        This function returns the static directories.\n
        """
        return self.static_files_dirs

def add_static_dirs_to_relative_paths(static_files_dirs: List[Path], relative_paths: List[Path]) -> List[Path]:
    """
    This function adds the static directories to the relative paths.\n
    It receives a List of paths to the static files directories and a List of relative paths.\n
    It returns a List of paths to the static files directories.\n
    """

    final_paths: List[Path] = []
    
    for relative_path in relative_paths:
        for static_dir in static_files_dirs:
            if (static_dir / relative_path).exists():
                final_paths.append(static_dir / relative_path)
    
    return final_paths

def unite_files(template_name: str, files: List[str]) -> Path:
    """
    This function unites the css and scss files in only one, template_name.css and template_name.scss and return the local of them.\n
    """

    if files[0].endswith('.scss'):
        scss: bool = True
    elif files[0].endswith('.css'): 
        scss: bool = False
    else:
        raise ValueError(f"Unsupported file type in List: {files}")
    
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
def load_stylesheets(stylesheet: Dict[str, List[str]]) -> str:
    """
    This function compresses all the css and scss files in the List in only one file for the app.\n
    It receives a Dictionary with the keys 'css_files', 'scss_files' and 'template_name'.\n
    The values of the keys are Lists of strings with the paths of the files.\n
    The paths of the files are relative to the app's static directory.\n
    The files will be searched in the app's static directory and the global one.\n
    """

    # Typing the stylesheet Dict elements
    css_files: List[str]
    scss_files: List[str]
    template_name: List[str]

    # Validate the stylesheet Dictionary
    validation = Validator(stylesheet)

    css_files, scss_files, template_name = validation.return_if_ok()

    collector = StaticDirsCollector(STATICFILES_DIRS, MY_APPS)

    css_files = add_static_dirs_to_relative_paths(
        collector.return_static_dirs(),
        css_files,
    )

    scss_files = add_static_dirs_to_relative_paths(
        collector.return_static_dirs(),
        scss_files,
    )

    Validator.check_files_exist(css_files + scss_files)

    # Unite the css and scss files in only one file
    css_united_file: Path = unite_files(template_name[0], scss_files)
    scss_united_file: Path = unite_files(template_name[0], css_files)

    # Transform the css and scss files in strings
    css_united_string: str = css_file_to_css_string(css_united_file)
    scss_united_string: str = compile_scss_file_to_css_string(scss_united_file)

    # Compress the css and scss files
    stylesheet_united: str = compress_css(css_united_string + "\n" + scss_united_string)

    # Write the compressed file in the UNITED_DIR
    with open(UNITED_DIR / f"{template_name[0]}.css", 'w') as file:
        file.write(stylesheet_united)

    # Return the path of the compressed file in string format
    return str(UNITED_DIR / f"{template_name[0]}.css")