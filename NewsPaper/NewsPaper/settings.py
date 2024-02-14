import logging
import os
from pathlib import Path

from django.conf import settings
from django.core.mail import mail_admins

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nm#n@#e=#!(+a2)l^5&ql8+h7a0y!nw+cqmpj&oduh^=h_s$so'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'news',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_filters',
    'accounts',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    'django_apscheduler',

]

MANAGERS = (
    ('Vova', 'chesnov.vovan@gmail.com'),
    ('Volodya', 'vvinkyz@gmail.com'),
)

ADMINS = (
    ('Vladimir', 'vvinkyz@gmail.com'),
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# # Настройки логирования
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
#         },
#         'warnings': {
#             'format': '%(asctime)s - %(levelname)s - %(module)s - %(pathname)s - %(message)s'
#         },
#         'errors': {
#             'format': '%(asctime)s - %(levelname)s - %(module)s - %(pathname)s -%(message)s\n%(exc_info)s'
#         },
#         'security': {
#             'format': '%(asctime)s - %(levelname)s - %(module)s - %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose',
#             'filters': ['console_filter']
#         },
#         'general_file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'general.log',
#             'formatter': 'verbose',
#             'filters': ['file_filter']
#         },
#         'errors_file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'errors.log',
#             'formatter': 'errors',
#             'filters': ['errors_filter']
#         },
#         'security_file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': 'security.log',
#             'formatter': 'security',
#             'filters': ['security_filter']
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'warnings',
#             'filters': ['mail_filter']
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'general_file'],
#             'level': 'DEBUG' if settings.DEBUG else 'INFO',
#         },
#         'django.request': {
#             'handlers': ['errors_file', 'mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.server': {
#             'handlers': ['errors_file', 'mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.template': {
#             'handlers': ['errors_file'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.db.backends': {
#             'handlers': ['errors_file'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'django.security': {
#             'handlers': ['security_file'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#     },
#     'filters': {
#         'console_filter': {
#             '()': 'django.utils.log.RequireDebugTrue',
#         },
#         'file_filter': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'errors_filter': {
#             '()': 'logging.Filter',
#         },
#         'security_filter': {
#             '()': 'logging.Filter',
#             'name': 'django.security',
#         },
#         'mail_filter': {
#             '()': 'django.utils.log.CallbackFilter',
#             'callback': lambda record: True,
#         },
#     },
# }
#
#
# # Настройки отправки почты
# def mail_admins_error(record):
#     print("вызывалось!!!!")
#     if record.levelno >= logging.ERROR:
#         mail_admins(
#             subject='Error on your site',
#             message=record.getMessage(),
#         )
#     return True
#
#
# # Настройки отправки почты
# if not settings.DEBUG:
#     LOGGING['handlers']['mail_admins']['level'] = 'ERROR'
#
#     LOGGING['loggers']['django.request']['handlers'] = ['mail_admins']
#     LOGGING['loggers']['django.server']['handlers'] = ['mail_admins']
#     LOGGING['loggers']['django.template']['handlers'] = ['mail_admins']
#     LOGGING['loggers']['django.db.backends']['handlers'] = ['mail_admins']
#     LOGGING['loggers']['django.security']['handlers'] = ['mail_admins']
#
#     LOGGING['filters']['mail_filter']['callback'] = mail_admins_error

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

LANGUAGES = [
    ('en-us', 'English'),
    ('ru', 'Русский'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

SITE_ID = 1
LOGIN_REDIRECT_URL = "/posts"
LOGOUT_REDIRECT_URL = "/posts"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "kinopoisk.y4ndex3@yandex.ru"
EMAIL_HOST_PASSWORD = "hlavcjkvegbuqhge"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = 'NewsPortal. '
DEFAULT_FROM_EMAIL = "kinopoisk.y4ndex3@yandex.ru"

SERVER_EMAIL = "kinopoisk.y4ndex3@yandex.ru"

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files')
    }
}

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
