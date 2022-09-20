"""
Django settings for django_find_bananas project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


IS_HEROKU = "DYNO" in os.environ

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Ajouter un dossier statics ou collectstatic via une commande Heroku, mettre ça dans le fichier procfile
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'find_bananas.apps.FindBananasConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_find_bananas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'django_find_bananas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#STATIC_ROOT = (os.path.join(SITE_ROOT, 'static_files/'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Enable WhiteNoise's GZip compression of static assets.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:8000',
#     }
# }

# SESSION_ENGINE = "django.contrib.sessions.backends.cache"


# def get_cache():
#   import os
#   try:
#     servers = os.environ['MEMCACHIER_SERVERS']
#     username = os.environ['MEMCACHIER_USERNAME']
#     password = os.environ['MEMCACHIER_PASSWORD']
#     return {
#       'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
#         # TIMEOUT is not the connection timeout! It's the default expiration
#         # timeout that should be applied to keys! Setting it to `None`
#         # disables expiration.
#         'TIMEOUT': None,
#         'LOCATION': servers,
#         'OPTIONS': {
#           'binary': True,
#           'username': username,
#           'password': password,
#           'behaviors': {
#             # Enable faster IO
#             'no_block': True,
#             'tcp_nodelay': True,
#             # Keep connection alive
#             'tcp_keepalive': True,
#             # Timeout settings
#             'connect_timeout': 2000, # ms
#             'send_timeout': 750 * 1000, # us
#             'receive_timeout': 750 * 1000, # us
#             '_poll_timeout': 2000, # ms
#             # Better failover
#             'ketama': True,
#             'remove_failed': 1,
#             'retry_timeout': 2,
#             'dead_timeout': 30,
#           }
#         }
#       }
#     }
#   except:
#     return {
#       'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'
#       }
#     }

# CACHES = get_cache()

django_heroku.settings(locals())
