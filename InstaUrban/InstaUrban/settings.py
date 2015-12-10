"""
Django settings for InstaUrban project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_im)5w-dg3l)oz8qt4ze87#=4q75c5*5euu72h^i$gu!km-e37'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Location app
    'location_field',
    'bootstrap3',

    # Our apps
    'images',
    'users',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'InstaUrban.urls'

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
                # Python Social Auth Context Processors
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'InstaUrban.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTHENTICATION_BACKENDS = (
 # Facebook
 'social.backends.facebook.FacebookOAuth2',
 # Twitter
 'social.backends.twitter.TwitterOAuth',
 # Github
 'social.backends.github.GithubOAuth2',
 # Django
 'django.contrib.auth.backends.ModelBackend',
)

# Facebook Keys
SOCIAL_AUTH_FACEBOOK_KEY = '433184503541251'
SOCIAL_AUTH_FACEBOOK_SECRET = '87eb542a7778150ce401907a28e331db'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/"

# Twitter Keys
SOCIAL_AUTH_TWITTER_KEY = 'uoAvDc7Kswfd3bOG82pPzH9q1'
SOCIAL_AUTH_TWITTER_SECRET = '5njZ6syrQmr4XfBRfGeptRSO4SxPDEucaYjnXX5GaN2W14es45'

# Github Keys
SOCIAL_AUTH_GITHUB_KEY = 'b4546db19c9bdd7c5742'
SOCIAL_AUTH_GITHUB_SECRET = '4e6531bf158ae3a3ce8fe13fad87013e4db605bc'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)
STATIC_ROOT = 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = (
    os.path.join(BASE_DIR, "media")
)
