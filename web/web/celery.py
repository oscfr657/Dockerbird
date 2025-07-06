import os

from celery import Celery
from celery.utils.log import get_task_logger

from django.core.management import call_command


logger = get_task_logger(__name__)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web.settings")

app = Celery("web")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task
def publish_scheduled_pages():
    call_command("publish_scheduled", )
    logger.info("The publish_scheduled_pages task just ran.")

@app.task
def searchpromotions_garbage_collect():
    call_command("searchpromotions_garbage_collect", )
    logger.info("The searchpromotions_garbage_collect task just ran.")
