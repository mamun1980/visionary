from .base import *

# from decouple import config
ENV = config('SITE_ENV', 'dev')
print(f"{'*' * 10} loading {ENV} evironment settings {'*' * 10}")

SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data/db.sqlite3',
    }
}