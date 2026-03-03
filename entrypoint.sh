#!/bin/sh
set -e

/opt/venv/bin/gunicorn \
    server.asgi:application \
    --bind 127.0.0.1:8000 \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker &

echo "Waiting Gunicorn to start..."
while ! nc -z 127.0.0.1 8000; do
  sleep 1
done
echo "Gunicorn its ready, starting nginx..."

exec nginx -g "daemon off;"