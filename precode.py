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

from server.settings import BASE_DIR
from pathlib import Path
from typing import List, TextIO

import sys
import os
import subprocess

HEADER_PY = """\
\"\"\" 
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
\"\"\"
"""

HEADER_CSS_SCSS = """\
/* 
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
*/
"""
HEADER_HTML = """\
<!-- 
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
-->
"""

class PreCodeExecutionError(Exception):
    """
    Custom exception for errors in the PreCodeExecution class.
    """
    def __init__(self, message: str) -> None:
        """
        Initialize the PreCodeExecutionError with a message.
        """
        self.message = message
        return super().__init__(message)
    
    def __repr__(self) -> str:
        """
        Return the string representation of the error.
        """
        return f"PreCodeExecutionError: {self.message}"
    
    def __str__(self) -> str:
        """
        Makes the same that __repr__.
        """
        return self.__repr__()

def save_log(string: str) -> None:
    """
    Save a log message to a file.
    :param string: The log message to save.
    :raises PreCodeExecutionError: If there is an error writing to the log file.
    :return: None
    """
    try:
        with open(".log", "a", encoding="utf-8") as log_file:
            log_file.write(string + "\n")
    except Exception as e:
        raise PreCodeExecutionError(
            f"Error in precode.py in method save_log:\n{e}"
        )

def _add_licence_header(file_path) -> None:
    """
    Add a license header to the file if it doesn't already exist.
    """
    with open(file_path, 'r+', encoding='utf-8') as f:

        content = f.read()

        if file_path.endswith('.py') and HEADER_PY not in content:
            f.seek(0, 0)
            f.write(HEADER_PY + "\n" + content)
            save_log(f'Header added to: {file_path}')

        elif file_path.endswith(('.css', '.scss')) and HEADER_CSS_SCSS not in content:
            f.seek(0, 0)
            f.write(HEADER_CSS_SCSS + "\n" + content)
            save_log(f'Header added to: {file_path}')

        elif file_path.endswith('.html') and HEADER_HTML not in content:
            f.seek(0, 0)
            f.write(HEADER_HTML + "\n" + content)
            save_log(f'Header added to: {file_path}')


def _is_file_ignored(file_path, gitignore) -> bool:
    """
    Check if the file is ignored by .gitignore.
    """
    return gitignore(file_path)

class InstallationError(Exception):
    """
    Custom exception for errors during the installation of packages.
    """
    def __init__(self, message: str) -> None:
        """
        Initialize the InstallationError with a message.
        """
        self.message = message
        return super().__init__(message)
    
    def __repr__(self) -> str:
        """
        Return the string representation of the error.
        """
        return f"InstallationError: {self.message}"
    
    def __str__(self) -> str:
        """
        Makes the same that __repr__.
        """
        return self.__repr__()

class InstallPackages(object):
    """
    This class manages the installation of packages using pip.
    It provides a method to install a list of packages and handle errors.
    """
    @staticmethod   
    def update_requirements_file(requirements_path: Path | None):
        # Update or create the requirements.txt
        requirements_exists: bool = (
            requirements_path is None or \
            not requirements_path.exists()
        )
        
        new_requirements_path: Path = Path()
        
        if requirements_exists:
            
            new_requirements_path: Path = BASE_DIR / 'requirements.txt'
            
            with open(new_requirements_path, 'w', encoding='utf-8') as f:
                f.write("# This file is automatically generated by the precode.py script.\n")
                f.write("# Do not edit this file manually.\n")
        
        try:

            installed_packages = subprocess.check_output([sys.executable, '-m' ,'pip', 'freeze']).decode('utf-8')

            if requirements_exists:
                
                with open(new_requirements_path, 'w', encoding='utf-8') as f:
                    f: TextIO
                    f.write(installed_packages)
            
            else:
                
                if requirements_path is None:
                    raise InstallationError("Requirements Path is None")

                with open(requirements_path, 'w', encoding='utf-8') as f:
                    f: TextIO
                    f.write(installed_packages)

            save_log(f'File {requirements_path} updated with installed packages.')

        except Exception as e:

            InstallationError(f'Error updating {requirements_path}: {e}')
    
    @staticmethod
    def find_packages() -> List[str]:
        """
        Find all packages in the requirements.txt file.
        :return: List of package names.
        """
        try:
            with open('requirements.txt', 'r', encoding='utf-8') as f:
                packages = [line.strip() for line in f if line.strip()]
            return packages

        except FileNotFoundError:
            raise InstallationError("requirements.txt file not found.")
        
        except Exception as e:
            raise InstallationError(f"An unexpected error occurred: {e}")

    @staticmethod
    def install_packages(packages: List[str]) -> None:
        """
        Install the given packages using pip.

        :param packages: List of package names to install.
        """
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *packages])

        except subprocess.CalledProcessError as e:
            raise InstallationError(f"Error installing package: {e}")
        
        except Exception as e:
            raise InstallationError(f"An unexpected error occurred: {e}\n\n")

class PreCodeExecution(object):
    """
    This class manages the addition of license headers to files in a directory.
    It also updates the requirements.txt file with installed packages.

    This class is designed to be used in a pre-code execution phase,
    where it ensures that all files have the appropriate license headers
    and that the requirements.txt file is up to date.
    It uses the gitignore_parser library to check if files are ignored
    by the .gitignore file, and it uses subprocess to run pip freeze
    to get the list of installed packages.

    The class has two static methods:
    - add_license_headers: This method walks through the directory,
      checks each file, and adds the appropriate license header if needed.

    - update_requirements_file: This method updates or creates the
      requirements.txt file with the list of installed packages.

    The class is designed to be run as a script, and it will save_log
    messages to the console indicating which files have been updated
    and if any errors occurred during the process.
    """

    @staticmethod
    def add_licence_headers():
        try:
            # Load the .gitignore
            import gitignore_parser

            gitignore_path = os.path.join(BASE_DIR, '.gitignore')
            gitignore = gitignore_parser.parse_gitignore(gitignore_path)

            for root, dirs, files in os.walk(BASE_DIR):
                # Ignore the 'docs' folder
                if 'docs' in dirs:
                    dirs.remove('docs')

                for file in files:
                    file_path = os.path.join(root, file)

                    # Ignore the COPYING.txt file
                    if file == 'COPYING.txt':
                        continue

                    # Ignore the __init__ python files
                    if file == '__init__.py':
                        continue

                    # Check if the file is ignored by .gitignore
                    if _is_file_ignored(file_path, gitignore):
                        continue

                    # Check if the file is a text file (UTF-8)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            f.read()  # Try to read the file
                        _add_licence_header(file_path)

                    except (UnicodeDecodeError, FileNotFoundError):
                        # Ignore files that are not UTF-8 or cannot be found
                        continue

        except Exception as e:
            raise PreCodeExecutionError(
                f"Error in precode.py in method add_licence of class PreCodeExecution:\n{e}"
            )