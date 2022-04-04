from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command


logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")


@shared_task
def publish_scheduled_pages():
    call_command("publish_scheduled_pages", )
    logger.info("The publish_scheduled_pages task just ran.")


@shared_task
def search_garbage_collect():
    call_command("search_garbage_collect", )
    logger.info("The search_garbage_collect task just ran.")
