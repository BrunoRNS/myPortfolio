#!/bin/bash

docker pull python:3.11-slim-bookworm
docker pull nginx:1.25-bookworm
docker pull redis:7-bookworm

docker run --rm -v ${PWD}/app:/app python:3.11-slim-bookworm \
    sh -c "pip install --upgrade pip && pip install -r /app/requirements.txt"

docker scan --accept-license --file app/Dockerfile python:3.11-slim-bookworm
docker scan --accept-license --file nginx/Dockerfile nginx:1.25-bookworm
docker scan --accept-license redis:7-bookworm