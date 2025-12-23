FROM python:3.11-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    DEBUG=False
    
RUN apk add --no-cache \
        nginx \
        bash \
        ca-certificates \
        libffi \
        libffi-dev \
        openssl \
        openssl-dev \
        libsodium \
        linux-headers \
        gcc \
        musl-dev \
        cargo \
    && python -m venv /opt/venv \
    && addgroup -S nginxgroup \
    && adduser -S nginxuser -G nginxgroup \
    && mkdir -p \
        /run/nginx \
        /var/log/nginx \
        /var/lib/nginx \
    && chown -R nginxuser:nginxgroup \
        /run/nginx \
        /var/log/nginx \
        /var/lib/nginx

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput \
    && find . -type f \( -name '*.env' -o -name '*.secret' \) -delete

RUN rm -f /etc/nginx/http.d/default.conf
COPY nginx.conf /etc/nginx/nginx.conf

COPY entrypoint.sh /app/entrypoint.sh
RUN chown nginxuser:nginxgroup /app/entrypoint.sh \
    && chmod 550 /app/entrypoint.sh \
    && chown -R nginxuser:nginxgroup /app

EXPOSE 8080

USER nginxuser

ENTRYPOINT ["/app/entrypoint.sh"]
