FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

RUN python -m venv $VIRTUAL_ENV

COPY requirements.txt .
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

COPY . .

RUN /opt/venv/bin/python manage.py migrate

RUN /opt/venv/bin/python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["/opt/venv/bin/gunicorn", "--bind", "0.0.0.0:8000", "server.wsgi"]