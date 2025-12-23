#!/bin/sh
set -e

 /opt/venv/bin/gunicorn \
    server.asgi:application \
    --bind 127.0.0.1:8000 \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker &

exec nginx -g "daemon off;"
