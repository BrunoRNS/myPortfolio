FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV DEBUG=False

RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx python3-venv && \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv $VIRTUAL_ENV

RUN groupadd -r nginxgroup && \
    useradd -r -g nginxgroup -s /bin/false nginxuser

RUN mkdir -p /run/nginx && \
    chown -R nginxuser:nginxgroup /run/nginx /var/log/nginx /var/lib/nginx

WORKDIR /app

COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN /opt/venv/bin/python manage.py collectstatic --noinput && \
    find . -type f -name '*.env' -delete && \
    find . -type f -name '*.secret' -delete

RUN rm -f /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/nginx.conf

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod 755 /app/entrypoint.sh

RUN chown -R nginxuser:nginxgroup /app

EXPOSE 8080

USER nginxuser

ENTRYPOINT ["/app/entrypoint.sh"]
