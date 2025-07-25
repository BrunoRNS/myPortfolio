#!/bin/bash

PORT=${PORT:-8080}

sed -i "s/listen 8080;/listen $PORT;/" /etc/nginx/nginx.conf

mkdir -p /run/nginx
chown nginxuser:nginxgroup /run/nginx

/opt/venv/bin/gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --worker-class gthread \
    --threads 2 \
    --timeout 30 \
    server.wsgi &

sleep 5

exec nginx -g "daemon off;"
