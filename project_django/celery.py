import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_django.settings')

from django.conf import settings

app = Celery('celery_realtime')

app.config_from_object('django.conf.settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    BROKER_URL = 'redis://localhost:6379/0',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
)