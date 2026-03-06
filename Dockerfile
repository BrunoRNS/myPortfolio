FROM python:3.11-slim AS builder
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc python3-dev && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip wheel && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx && rm -rf /var/lib/apt/lists/* && \
    addgroup --system nginxgroup && adduser --system --no-create-home --group nginxuser

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBUG=False

WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY . .
RUN python manage.py collectstatic --noinput && \
    rm -f /etc/nginx/sites-enabled/default && \
    mkdir -p /var/lib/nginx/body /var/lib/nginx/proxy /var/log/nginx /run/nginx && \
    chown -R nginxuser:nginxgroup /app /var/lib/nginx /var/log/nginx /run/nginx /etc/nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY proxy_params /etc/nginx/proxy_params
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

RUN chown nginxuser:nginxgroup /etc/nginx/nginx.conf /etc/nginx/proxy_params

EXPOSE 8080
USER nginxuser
ENTRYPOINT ["/app/entrypoint.sh"]
