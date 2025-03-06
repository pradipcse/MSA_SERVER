import os

ENVIRONMENT = os.getenv('DJANGO_ENV', 'dev')  # Change to 'prod' in production

if ENVIRONMENT == 'prod':
    from .prod import *
else:
    from .dev import *
