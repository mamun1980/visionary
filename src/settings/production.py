from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["*"]


DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': config('DB_NAME', 'jm002'),
        'USER': config('DB_USER_NAME', 'postgres'),
        'PASSWORD': config('DB_USER_PASSWORD', 'qweqwe123'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default=5432, cast=int)
    }
}