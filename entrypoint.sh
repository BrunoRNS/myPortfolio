#!/bin/bash
set -e

echo "Starting Gunicorn..."
gunicorn server.asgi:application \
    --bind 127.0.0.1:8000 \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker \
    --max-requests 1000 \
    --max-requests-jitter 50 &

wait_for_port() {
    local host=$1 port=$2 timeout=$3
    local start_time=$(date +%s)
    while ! timeout 1 bash -c "echo > /dev/tcp/$host/$port" 2>/dev/null; do
        sleep 1
        if (($(date +%s) - start_time >= timeout)); then
            echo "Timeout waiting $host:$port"
            exit 1
        fi
    done
}

wait_for_port 127.0.0.1 8000 30
echo "Gunicorn ready, starting nginx..."
exec nginx -g "daemon off;"
