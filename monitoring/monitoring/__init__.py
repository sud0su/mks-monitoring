import os

from .celery_app import app as celery_app

# __version__ = (2, 8, 0, 'final', 1)
__all__ = ['celery_app']


class MonitoringException(Exception):
    """Base class for exceptions in this module."""
    pass

# def get_version():
#     import monitoring.version
#     return monitoring.version.get_version(__version__)

def main(global_settings, **settings):
    from django.core.wsgi import get_wsgi_application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.get('django_settings'))
    app = get_wsgi_application()
    return app
