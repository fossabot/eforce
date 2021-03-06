"""
Django settings for eforce project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')lhngr8##))4x+ew6gh^6v))zd^10rmsxpshz^#-4v1*c&nn=='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'eforce_api',
    'eforce_front',
    'sw_layer',
    'rest_framework',
    'bootstrap3',
    'storages',
    'channels',
]

if os.environ.get('SELF_HOSTING'):
    MEDIA_ROOT = "/var/www/media"
    MEDIA_URL = "/media/"
else:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
GOOGLE_SERVICE_API_KEY = os.environ.get('GOOGLE_SERVICE_API_KEY')
CMO_AUTHENTICATION_KEY = os.environ.get('CMO_AUTHENTICATION_KEY', 'VERY-SECRET-KEY')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = [
    '--cover-erase',
    '--cover-package=eforce_api',
    '--cover-package=eforce_front',
]

MIDDLEWARE_CLASSES = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'PAGE_SIZE': 20
}

ROOT_URLCONF = 'eforce.urls'

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

WSGI_APPLICATION = 'eforce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'eforce'),
        'USER': os.environ.get('DB_USER', 'eforceapp'),
        'PASSWORD': 'qwe123qwe123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_REDIRECT_URL = '/home/'
LOGIN_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# django-bootstrap3 settings
BOOTSTRAP4 = {
    'jquery_url': os.path.join(STATIC_URL, 'bower_components/jquery/dist/jquery.min.js'),
    'base_url': os.path.join(STATIC_URL, 'bower_components/bootstrap/dist/'),
    'css_url': None,
    'javascript_url': None,
    'include_jquery': True,
    'javascript_in_head': True,
}

# channels settings
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "ROUTING": "eforce.routing.channel_routing",
    },
}

# eforceapp constant
EF_HQ_ROLENAME = 'EF_HQ'
CONST_CMO_DOMAIN = "http://" + os.environ.get('CMO_API_URL', '220.255.94.107:628') + "/"
