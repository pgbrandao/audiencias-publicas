"""
Django settings for audiencias_publicas project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config, Csv
from dj_database_url import parse as db_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('DJANGO_SECRET_KEY', default='secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS',
                       cast=Csv(lambda x: x.strip().strip(',').strip()),
                       default='*')

# Application definition

INSTALLED_APPS = (
    'apps.core',
    'apps.accounts',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'crispy_forms',
    'corsheaders',
    'debug_toolbar',

    'djangobower',
    'compressor',
    'compressor_toolkit',
    'django_q', # not used, but don't remove
    'channels',
    'channels_presence',
)

SITE_ID = 1

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'GET',
    'OPTIONS'
)

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'PAGE_SIZE': 10
}

QUESTION_MIN_UPVOTES = config('QUESTION_MIN_UPVOTES', default=3, cast=int)
GOOGLE_ANALYTICS_ID = config('GOOGLE_ANALYTICS_ID', default='')
OLARK_ID = config('OLARK_ID', default='')
WEBSERVICE_URL = config('WEBSERVICE_URL', default='')

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'apps.accounts.middlewares.AudienciasRemoteUser',
)

ROOT_URLCONF = 'audiencias_publicas.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'apps.core.processors.analytics',
            ],
        },
    },
]

WSGI_APPLICATION = 'audiencias_publicas.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = dict(default=config(
    'DATABASE_URL', cast=db_url,
    default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'))
)


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGES = (
    ('en', 'English'),
    ('pt-br', 'Brazilian Portuguese'),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = config('STATIC_URL', default='/static/')

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'static'))

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
]

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static')

BOWER_INSTALLED_APPS = [
    'jquery#~2.2.0',
    'foundation-sites#~6.2.4',
    'mixitup#~2.1.11',
    'https://github.com/labhackercd/fontastic-labhacker.git',
    'https://github.com/joewalnes/reconnecting-websocket.git',
]

BOWER_PATH = os.path.join(BASE_DIR, 'node_modules/.bin/bower')
BROWSERIFY = os.path.join(BASE_DIR, 'node_modules/.bin/browserify')

COMPRESS_NODE_MODULES = os.path.join(BASE_DIR, 'node_modules')
COMPRESS_NODE_SASS_BIN = os.path.join(BASE_DIR, 'node_modules/.bin/node-sass')
COMPRESS_POSTCSS_BIN = os.path.join(BASE_DIR, 'node_modules/.bin/postcss')

COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'compressor_toolkit.precompilers.SCSSCompiler'),
    ('text/es6', BROWSERIFY + ' {infile} -t babelify --outfile {outfile}')
]

COMPRESS_ROOT = os.path.join(BASE_DIR, 'static')

LIBSASS_SOURCEMAPS = 'DEBUG'

# Authentication stuffs

URL_PREFIX = config('URL_PREFIX', default='')
FORCE_SCRIPT_NAME = config('FORCE_SCRIPT_NAME', default='')
LOGIN_URL = config('LOGIN_URL', default='/login/')
LOGIN_REDIRECT_URL = config('LOGIN_REDIRECT_URL', default='/')
LOGOUT_REDIRECT_URL = config('LOGOUT_REDIRECT_URL', default='/')

SESSION_COOKIE_NAME = config('SESSION_COOKIE_NAME', default='sessionid')
SESSION_COOKIE_PATH = config('SESSION_COOKIE_PATH', default='/')

# Social auth
if config('ENABLE_REMOTE_USER', default=0, cast=bool):
    AUTHENTICATION_BACKENDS = (
        'apps.accounts.backends.AudienciasAuthBackend',
    )
else:
    AUTHENTICATION_BACKENDS = (
        'rules.permissions.ObjectPermissionBackend',
        'django.contrib.auth.backends.ModelBackend',
    )

# Email configuration

EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='')

CHANNEL_LAYERS = {
    "default": {
        # This example app uses the Redis channel layer implementation asgi_redis
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "ROUTING": "apps.core.routing.channel_routing",
    },
}

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO'
        },
        'chat': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG',
        },
    },
}

WORDS_BLACK_LIST = config('WORDS_BLACK_LIST',
                          cast=Csv(lambda x: x.strip().strip(',').strip()),
                          default='')

NOTIFICATION_EMAIL_LIST = config(
    'NOTIFICATION_EMAIL_LIST',
    cast=Csv(lambda x: x.strip().strip(',').strip()),
    default=''
)
