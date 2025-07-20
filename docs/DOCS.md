# Bruno RNS Portfolio — Developer Documentation

## Table of Contents

- [1. Project Structure](#1-project-structure)
- [2. Environment Setup](#2-environment-setup)
- [3. Configuration](#3-configuration)
- [4. Core Components](#4-core-components)
  - [4.1 Django App: `home`](#41-django-app-home)
  - [4.2 Services](#42-services)
  - [4.3 Views](#43-views)
  - [4.4 Forms](#44-forms)
  - [4.5 Static & Templates](#45-static--templates)
  - [4.6 Env Loading](#46-env-loading)
  - [4.7 Caching & Rate Limiting](#47-caching--rate-limiting)
  - [4.8 Pre-Code Automation](#48-pre-code-automation)
  - [4.9 Testing & CI](#49-testing--ci)
- [5. Design Patterns Used](#5-design-patterns-used)
- [6. Continuous Integration](#6-continuous-integration)
- [7. Deployment](#7-deployment)
- [8. License](#8-license)

---

## 1. Project Structure

```sh
myPortfolio/
├── home/                # Main Django app
│   ├── forms/           # Django forms
│   ├── services/        # Backend service logic
│   ├── static/          # Static files (JS, CSS, images)
│   ├── templates/       # HTML templates
│   ├── views/           # Django views
│   └── apps.py          # App configuration
├── server/              # Django project settings, URLs, WSGI
├── tests/               # Test scripts
├── .github/             # GitHub Actions workflows
├── docs/                # Documentation
├── requirements.txt     # Python dependencies
├── Dockerfile           # Containerization
├── manage.py            # Django management script
├── .env-example         # Example environment variables
└── README.md            # Project overview
```

---

## 2. Environment Setup

- **Python Version:** 3.11 or 3.12
- **Virtual Environment:** Recommended for dependency isolation
- **Redis:** Required for caching and rate limiting

### Quickstart

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env-example .env
# Edit .env with your secrets
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

---

## 3. Configuration

Sensitive settings are loaded from `.env` using `python-dotenv`.

**Required variables:**

- `SECRET_KEY`
- `GITHUB_TOKEN` (for GitHub API access)
- `NOTIFICATION_TOKEN` (for creating issues/notifications)
- `DEBUG`
- `ALLOWED_HOSTS`
- `REDIS_URL`

See `.env-example` for format.

---

## 4. Core Components

### 4.1 Django App: `home`

Centralizes portfolio logic, forms, views, and service integration.

- **`apps.py`**: Django app configuration.
- **`forms/forms.py`**: Contains `ContactForm` for validating and sanitizing user input.

### 4.2 Services

Located in `home/services/`, these modules encapsulate backend logic:

- **`getGithubData.py`**: Fetches repositories and metadata from GitHub using PyGithub.
- **`sendMessage.py`**: Sends notifications by creating GitHub issues in a designated repo. Includes spam prevention logic.
- **`changeToDjangoStatic.py`**: Converts static paths in HTML to Django `{% static %}` tags.

### 4.3 Views

Located in `home/views/`:

- **`home.py`**: Renders the main portfolio page. Uses caching and rate limiting for performance and security.
- **`notification.py`**: Handles POST requests from the contact form. Validates input, checks for spam, and triggers notification service.

### 4.4 Forms

- **`ContactForm`**: Validates name, email, and message fields. Used for both frontend and backend validation.

### 4.5 Static & Templates

- Static files served via Django's staticfiles and `whitenoise` middleware.
- Templates use Django's template language and `{% static %}` for asset paths.

### 4.6 Env Loading

- **Environment Variables:** Managed via `.env` and loaded with `python-dotenv`.
- **Settings:** All sensitive and environment-specific settings are centralized in `server/settings.py`.

### 4.7 Caching & Rate Limiting

- **Caching:** Uses Django's cache framework with Redis backend for performance.
- **Rate Limiting:** Implemented via `django_ratelimit` decorators on views to prevent abuse.

### 4.8 Pre-Code Automation

- **`precode.py`**: Automates license header insertion and requirements management before code execution.

### 4.9 Testing & CI

- **Unit Tests:** Located in `home/tests/`.
- **Test Automation:** `tests/testDjango.sh` script for local testing.
- **Continuous Integration:** GitHub Actions workflow in `.github/workflows/django.yml`.

---

## 5. Design Patterns Used

- **Service Layer Pattern:** Business logic is encapsulated in service modules (`home/services/`), separating it from views and forms.
- **Factory Pattern:** Django forms and views act as factories for creating validated objects and HTTP responses.
- **Decorator Pattern:** Used for rate limiting and caching via decorators (`@ratelimit`, `@cache_page`).
- **Singleton Pattern:** Django settings and cache are singletons, ensuring consistent configuration and state.
- **Template Method Pattern:** Django's template system allows for flexible rendering and extension of HTML templates.
- **Command Pattern:** Management commands and scripts (like `precode.py` and `manage.py`) encapsulate operations as commands.

These patterns maintain separation of concerns, improve testability, and support scalability and maintainability.

---

## 6. Continuous Integration

- **GitHub Actions:** Runs tests for Python 3.11 and 3.12, installs dependencies, and executes Django's test suite automatically on push and PR.

---

## 7. Deployment

- **Docker:** Use the provided `Dockerfile` for containerized deployment.
- **Gunicorn:** Production server runs via Gunicorn.
- **Static Files:** Collected with `manage.py collectstatic`.

### Example Docker Usage

```sh
docker build -t myportfolio .
docker run -p 8000:8000 --env-file .env myportfolio
```

---

## 8. License

This project is licensed under the GNU General Public License v3.0.  
See [LICENSE.md](LICENSE.md) for details.

---

> For further questions or contributions, please open an issue or a pull request, and contact Bruno RNS.
