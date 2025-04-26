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

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from server.settings import BASE_DIR

from precode import InstallPackages, PreCodeExecution

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':

    # Delete old log file if it exists
    os.unlink(os.path.join(os.path.dirname(__file__), '.log')) if os.path.exists(os.path.join(os.path.dirname(__file__), '.log')) else None

    # Create or find a requirements.txt file
    InstallPackages.update_requirements_file(BASE_DIR / 'requirements.txt' if os.path.exists(BASE_DIR / 'requirements.txt') else None)

    # Install required packages
    InstallPackages.install_packages(InstallPackages.find_packages())

    # Execute pre-code
    PreCodeExecution.add_licence_headers()

    # Main function to run the Django server
    main()