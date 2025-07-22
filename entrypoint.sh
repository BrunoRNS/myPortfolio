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
    --access-logfile - \
    server.wsgi &

sleep 5

unset SECRET_KEY
unset GITHUB_TOKEN
unset NOTIFICATION_TOKEN
unset DEBUG
unset ALLOWED_HOSTS
unset REDIS_URL

exec nginx -g "daemon off;"
