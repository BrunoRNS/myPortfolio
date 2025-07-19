#!/bin/bash

set -e

cd "$(dirname "$0")"

cd ..

virtualenv venv

venv/bin/pip install -r requirements.txt
venv/bin/python manage.py test

rm -rf venv