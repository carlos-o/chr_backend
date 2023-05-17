"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import environs
import logging.config
import os
from pathlib import Path
from django.utils.log import DEFAULT_LOGGING


env = environs.Env()
environs.Env.read_env()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

URL = env('URL')

NETWORK_API_URL = "https://api.citybik.es/v2/networks/{}"

SNIFA_URL = "https://snifa.sma.gob.cl{}"

ALLOWED_HOSTS = []


# Application definition

# Application definition
DJANGO_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]

LOCAL_APPS = [
	'network',
	'snifa',
]

THIRD_PARTY_APPS = [
	'corsheaders',
	'django_jsonform',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.urls"

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

WSGI_APPLICATION = "src.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'HOST': env('DB_HOST'),
		'DATABASE_PORT': env('DB_PORT'),
		'NAME': env('DB_NAME'),
		'USER': env('DB_USER'),
		'PASSWORD': env('DB_PASSWORD')
	}
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Santiago"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Cors Configurations
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = False
CORS_ALLOW_HEADERS = (
	'accept',
	'accept-encoding',
	'authorization',
	'content-type',
	'dnt',
	'origin',
	'user-agent',
	'x-csrftoken',
	'x-requested-with',
	'Access-Control-Allow-Origin',
)
CORS_ORIGIN_WHITELIST = (
	'http://localhost:8080',
	'http://127.0.0.1:8080',
	'http://localhost:3000',
	'http://127.0.0.1:3000',
	'http://localhost:3001',
	'http://127.0.0.1:3001',
)

CORS_ALLOW_METHODS = (
	'DELETE',
	'GET',
	'OPTIONS',
	'PATCH',
	'POST',
	'PUT',
)

# Log configuration
log_path = os.path.join(BASE_DIR)
LOG_FOLDER = os.path.join(log_path, 'logs')
LOG_FILE_INFO = LOG_FOLDER + '/' + 'info.log'
LOG_FILE_ERRORS = LOG_FOLDER + '/' + 'errors.log'
LOG_FILE_DJANGO = LOG_FOLDER + '/' + 'django.log'
LOGGING_CONFIG = None
LOG_LEVEL = 'DEBUG' if DEBUG else 'INFO'

if not os.path.exists(LOG_FOLDER):
	os.makedirs(LOG_FOLDER)

logging.config.dictConfig({
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'default': {
			'format': '%(asctime)s - %(name)s - [%(levelname)s] -> %(message)s',
		},
		'django.server': DEFAULT_LOGGING['formatters']['django.server'],
	},
	'handlers': {
		'console': {
			'class': 'logging.StreamHandler',
			'level': LOG_LEVEL,
			'formatter': 'default',
		},
		'django_error': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'DEBUG',
			'formatter': 'default',
			'filename': LOG_FILE_DJANGO,
			'maxBytes': 10485760,
			'backupCount': 20,
			'encoding': 'utf8'
		},
		'info_file_handler': {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'DEBUG',
			'formatter': 'default',
			'filename': LOG_FILE_INFO,
			# 10 MB
			'maxBytes': 10485760,
			'backupCount': 20,
			'encoding': 'utf8'
		},
		"error_file_handler": {
			'class': 'logging.handlers.RotatingFileHandler',
			'level': 'ERROR',
			'formatter': 'default',
			'filename': LOG_FILE_ERRORS,
			# 10 MB
			'maxBytes': 10485760,
			'backupCount': 20,
			'encoding': 'utf8'
		},
		'django.server': DEFAULT_LOGGING['handlers']['django.server'],
	},
	'loggers': {
		'src': {
			'level': LOG_LEVEL,
			'handlers': ['console', 'info_file_handler', 'error_file_handler'],
			'propagate': False,
		},
		'django': {
			'handlers': ['console'],
			'level': 'INFO',
			'propagate': True,
		},
		'django.request': {
			'handlers': ['django_error', 'console'],
			'level': LOG_LEVEL,
			'propagate': False,
		},
		'django.db.backends': {
			'handlers': ['console'],
			'level': 'ERROR',
			'propagate': True,
		},
		'django.server': DEFAULT_LOGGING['loggers']['django.server'],
	}
})