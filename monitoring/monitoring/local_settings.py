import os
from monitoring.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mksmonitoring',
        'USER': 'postgres',
        'PASSWORD': 'rencong',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_DIRS = ( os.path.join(PROJECT_DIR, "static"), )
