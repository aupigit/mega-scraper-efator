from datetime import timedelta
from pathlib import Path
import os

from prettyconf import config
from utils.settings import get_project_package

BASE_DIR = Path(__file__).absolute().parents[2]
PROJECT_DIR = Path(__file__).absolute().parents[1]

SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DJANGO_DEBUG", default=False, cast=config.boolean)
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="*", cast=config.list)
# CORS_ALLOWED_ORIGINS = config("DJANGO_CORS_ALLOWED_ORIGINS", default="", cast=config.list)
CSRF_TRUSTED_ORIGINS = config("DJANGO_CSRF_TRUSTED_ORIGINS", default="", cast=config.list)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = "pt-br"
ROOT_URLCONF = "app.urls"

_project_package = get_project_package(PROJECT_DIR)
ROOT_URLCONF = "{}.urls".format(_project_package)
WSGI_APPLICATION = "{}.wsgi.application".format(_project_package)
LOG_REQUEST_ID_HEADER = "HTTP_X_REQUEST_ID"
HTTPS_REQUIRED = config("HTTPS_REQUIRED", default=True, cast=config.boolean)

# Media & Static
MEDIA_URL = "/media/"
MEDIA_ROOT = PROJECT_DIR / "mediafiles"


STATIC_URL = "/static/"
STATIC_ROOT = PROJECT_DIR / "staticfiles"

# STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

DATABASES = {
    "default": {
        "ENGINE": config("DJANGO_DB_ENGINE"),
        "NAME": config("DJANGO_DB_NAME"),
        "USER": config("DJANGO_DB_USER"),
        "PASSWORD": config("DJANGO_DB_PASSWORD"),
        "HOST": config("DJANGO_DB_HOST"),
        "PORT": config("DJANGO_DB_PORT"),
        "TIME_ZONE": config("DJANGO_DB_TIME_ZONE"),
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"