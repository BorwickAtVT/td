"""
Django settings for td project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

INSTALLED_APPS = apps_from('app') + (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lib.middleware.UsernameInEnvMiddleware',
)

ROOT_URLCONF = 'td.urls'

WSGI_APPLICATION = 'td.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

import os

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT_DIR, 'templates'),
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# This is rarely needed, but exists for Docker-izing this code:
if os.environ.get('MIGRATE_ONLY', False):
    SECRET_KEY = 'dummy'
else:
    import os
    SECRET_KEY = os.environ['SECRET_KEY']
    BEID = os.environ['BEID']
    WebServicesKey = os.environ['WEBSERVICESKEY']

    import tdapi
    TD_CONNECTION = tdapi.set_connection(
        tdapi.TDConnection(BEID=BEID,
                           WebServicesKey=WebServicesKey))


    TD_CLIENT_URL = os.environ['TD_CLIENT_URL']

    # this URL needs to end in '/':
    if TD_CLIENT_URL[-1] != '/':
        TD_CLIENT_URL += '/'
