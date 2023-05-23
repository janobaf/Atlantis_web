from .base import *
import os
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'Restaurante',
        'USER':'',
        'PASSWORD':'',
        'HOST': 'DESKTOP-5HUGSMT',
        'PORT':'',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.child('media')

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'arturo948661842@gmail.com'
EMAIL_HOST_PASSWORD = 'hjrekawrcrqrcdgn'
EMAIL_PORT = 587