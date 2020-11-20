import datetime
import celery
from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.utils import timezone

from .bmx_client import get_series
from .models import Udi, Dollar


log = get_task_logger(__name__)


@shared_task
def get_series(**kwargs):
    """
    Task to get series data from Banxico
    """
    series = [settings.BMX_UDI_SERIE,
              settings.BMX_DOLLAR_SERIE]
    today = timezone.now().strftime('%Y-%m-%d')
    data = get_series(series, today, today, settings.BMX_TOKEN)
    if not data:
        log.info("Empty data from Endpoint ")
    # 
    for serie in data['bmx']['series']:
        if serie['idSerie'] == settings.BMX_UDI_SERIE:
            Udi.objects.insert_api_data(serie)
        # save dollar
        Dollar.objects.insert_api_data(serie)
    return True
