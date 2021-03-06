"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 3.0.dev20190908153532.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import django_heroku
import dj_database_url
import dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j-khsnkvnqi5+tf05lw9%e_lvn4^l(wf8pk$d5pbe9%h3r1ybi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'anket',
    'anketgonder',
    'crispy_forms',
    'bitly_api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
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

SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
TEMPLATE_DIRS = (
    os.path.join(SETTINGS_PATH, 'templates'),
)

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

EMAIL_HOST = "smtp.ttyazilim.net"

EMAIL_PORT = 587

EMAIL_HOST_USER = "info@ttyazilim.net"

EMAIL_HOST_PASSWORD = "Tolgahan123+"

STATIC_URL = '/static/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
del DATABASES['default']['OPTIONS']['sslmode']


#SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = False

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF= True

#CSRF_COOKIE_SECURE = False

X_FRAME_OPTIONS = 'DENY'

SECURE_HSTS_SECONDS = '60'

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True