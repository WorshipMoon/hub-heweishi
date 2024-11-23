"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from decouple import config
import os
from urllib.parse import urlparse


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("DJANGO_SECRET_KEY", cast=str)

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ["localhost", "127.0.0.1", "192.168.0.102", "localhub.amusi755.com"]

ALLOWED_HOSTS = [".amusi755.com", ".vape755.com"]
if DEBUG:
    ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "vnbase",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

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

WSGI_APPLICATION = "project.wsgi.application"


# CORS_URLS_REGEX = r"^/api/.*$"
CORS_ALLOWED_ORIGINS = []
ENV_CORS_ALLOWED_ORIGINS = config("CORS_ALLOWED_ORIGINS", cast=str, default="")
for origin in ENV_CORS_ALLOWED_ORIGINS.split(","):
    CORS_ALLOWED_ORIGINS.append(f"{origin}".strip().lower())

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8001",
#     "http://localhost:3001",
#     "https://zfbvnlocal.amusi755.com:3001",
# ]


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# tmpPostgres = urlparse(os.getenv("DATABASE_URL"))
# print(tmpPostgres.hostname)
DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME", "hub_web"),
        "USER": os.environ.get("DATABASE_USER", "sean"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "123456"),
        "HOST": os.environ.get("DATABASE_HOST", "hub-postgres"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": tmpPostgres.path.replace("/", ""),
    #     "USER": tmpPostgres.username,
    #     "PASSWORD": tmpPostgres.password,
    #     "HOST": tmpPostgres.hostname,
    #     "PORT": 5432,
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_ROOT = BASE_DIR / "static"

MAX_UPLOAD_SIZE = 3 * 1024 * 1024  # Maximum file upload size in bytes (3MB)
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# send_mail
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
# EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST_USER = "amusu.pain@gmail.com"
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "amusu.pain@gmail.com"


# 确保日志目录存在
LOGS_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOGS_DIR, exist_ok=True)
#  DEBUG、INFO、WARNING、ERROR 和 CRITICAL
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            # 'filename': '/app/logs/django.log',  # 确保这个路径在容器中是可写的
            "filename": os.path.join(
                BASE_DIR, LOGS_DIR, "django.log"
            ),  # 确保这个路径在容器中是可写的
            "formatter": "verbose",
        },
    },
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
            # "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            # "style": "{",
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
            # "format": "{levelname} {message}",
            # "style": "{",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
    "loggers": {
        "django": {  # 记录 Django 框架的所有
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
        #  'django.request': {
        #     'handlers': ['file'],
        #     'level': 'ERROR',
        #     'propagate': True,
        # },
        #  'myapp': {  # 自定义应用的日志配置
        #     'handlers': ['file'],
        #     'level': 'DEBUG',
        #     'propagate': True,
        # },
    },
}
