from decouple import config
ENV = config('SITE_ENV', 'dev')

if ENV == 'prod':
    print(f"{'*' * 10} loading {ENV} evironment settings {'*' * 10}")
    from .production import *
elif ENV == 'dev':
    from .dev import *