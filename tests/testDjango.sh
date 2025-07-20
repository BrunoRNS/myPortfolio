#!/bin/bash

#!/bin/bash
# Copyright (c) 2022, Bruno Rian Nunes de Souza
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 3, as published
# by the Free Software Foundation.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

# This script is used to test the Django part of the program.
# It creates a virtual environment, installs the dependencies and runs the tests.

set -e # Exit immediately if a command exits with a non-zero status

cd "$(dirname "$0")" # Change to the directory where the script is located

cd .. # Move to the parent directory

virtualenv venv # Create a virtual environment named 'venv'

venv/bin/pip install -r requirements.txt # Install dependencies from requirements.txt

venv/bin/python manage.py test # Run Django tests

rm -rf venv # Remove the virtual environment
