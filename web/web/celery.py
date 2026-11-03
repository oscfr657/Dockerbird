import os

from celery import Celery
from celery.utils.log import get_task_logger

from . import tasks


logger = get_task_logger(__name__)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

app = Celery("web")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
