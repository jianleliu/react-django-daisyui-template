"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from backend.settings.base import DEBUG

from django.core.wsgi import get_wsgi_application

if DEBUG:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.local')
else:
  os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings.production')

application = get_wsgi_application()
