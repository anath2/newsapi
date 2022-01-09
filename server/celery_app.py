from celery import Celery
from . import constants as c


celery_app = Celery("worker", broker=c.CELERY_BROKER)
