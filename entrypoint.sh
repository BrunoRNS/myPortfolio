#!/bin/bash

/opt/venv/bin/gunicorn \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --worker-class gthread \
    --threads 2 \
    --timeout 30 \
    --access-logfile - \
    server.wsgi &
    
exec nginx -g "daemon off;"
