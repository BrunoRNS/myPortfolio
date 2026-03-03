#!/bin/sh
set -e

/opt/venv/bin/gunicorn \
    server.asgi:application \
    --bind 127.0.0.1:8000 \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker \
    --max-requests 1000 \
    --max-requests-jitter 50 &

echo "Waiting Gunicorn to start..."
while ! nc -z 127.0.0.1 8000; do
  sleep 1
done
echo "Gunicorn its ready, starting nginx..."

exec nginx -g "daemon off;"