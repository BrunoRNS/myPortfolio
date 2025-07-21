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

RUN useradd --system --no-create-home appuser

WORKDIR /app

COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN /opt/venv/bin/python manage.py collectstatic --noinput && \
    find . -type f -name '*.env' -delete && \
    find . -type f -name '*.secret' -delete

RUN rm /etc/nginx/sites-enabled/default
COPY nginx.conf /etc/nginx/conf.d/app.conf

COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

RUN chown -R appuser:appuser /app /var/log/nginx /var/lib/nginx

EXPOSE 80

USER appuser

ENTRYPOINT ["/app/entrypoint.sh"]
