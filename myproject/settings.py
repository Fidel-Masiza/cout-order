"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x*%o4w2js7&rm_2u!__r$hbpbel9jm(1%*ww-+lyjw%dk3snu6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost' ,'*']
if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost' ,'*']
else:
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')

SITE_URL = 'http://127.0.0.1:8000' if DEBUG else 'https://cout-order.onrender.com'


# Application definition



import os
import dj_database_url

DEBUG = os.environ.get('DEBUG', False)  # Default to False for production





INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'rest_framework',
    'rest_framework.authtoken',
    'ckeditor',
    'ckeditor_uploader',

]








CKEDITOR_UPLOAD_PATH = "uploads/"



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = 'myproject.urls'

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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
   # 'default': {
     #   'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': BASE_DIR / 'db.sqlite3',
    #}
#}
#DATABASES = {
   # 'default': {
      #  'ENGINE': 'django.db.backends.postgresql',
      #  'NAME': 'dante',
      #  'USER': 'postgres',
       # 'PASSWORD': 'masizacreatives!3',
       # 'HOST': 'localhost',  # or the address of your database server
      #  'PORT': '5432',  # default port for PostgreSQL
   # }
#}
DATABASES = {
        'default' : dj_database_url.parse (' postgresql://my_db101_user:Ik76fwkHPuuTSLFwj5axbKUmCoIg4HIm@dpg-cqpeph3v2p9s73caurt0-a.oregon-postgres.render.com/my_db101')
        
        }


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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# myproject/settings.py

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fidelmasitsa03@gmail.com'  
EMAIL_HOST_PASSWORD = 'qkhq cenh zirv qonj'  
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CENTRAL_NOTIFICATION_EMAIL = 'betsuccor@gmail.com'  



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory to collect static files

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dante',
        'USER': 'postgres',
        'PASSWORD': 'masizacreatives!3',
        'HOST': 'localhost',  # or the address of your database server
        'PORT': '5432',  # default port for PostgreSQL
    }
}





ADMIN_EMAILS = [
    'goergew424@gmail.com',
    'admin2@example.com',
    'admin3@example.com',
    'admin4@example.com',
    'admin5@example.com',
]


PAYPAL_CLIENT_ID = 'AbtkUk0TVy-hfNj1EZG9mkwh5K4nHC_QeifnvJQp2v7EYe0fLq_sn2vy3bHbeGtzAvjVCG0TByt-zChw'
PAYPAL_CLIENT_SECRET ='EMVx7n8euV3m9Hpe0uyga0dQy_VevaUuDff8wQt0zUCQIDO4rGwDEVU4sVlJQGxffCKaF5WZdBhaerKL'
PAYPAL_MODE = 'live'  # or 'live' for production what is this paypal_mode? if i only have these  App name

