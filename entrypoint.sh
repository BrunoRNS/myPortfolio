#!/bin/sh
set -e

 /opt/venv/bin/gunicorn \
    server.asgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker &

exec nginx -g "daemon off;"
