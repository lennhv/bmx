import logging
from django_cron import CronJobBase, Schedule
from django.utils import timezone
from django.conf import settings

from .bmx_client import get_series
from .models import Udi, Dollar

log = logging.getLogger(__name__)


class BmxCronJob(CronJobBase):
    """ Cron job to syncs Banxico series data
    """
    RETRY_AFTER_FAILURE_MINS = 5
    RUN_AT_TIMES = ['06:00', '07:00', '08:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES,
                        retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'series.bmx_cron_job'    # a unique code

    def do(self):
        log.debug("start get series task")
        series = [settings.BMX_UDI_SERIE,
                  settings.BMX_DOLLAR_SERIE]
        today = timezone.now().strftime('%Y-%m-%d')
        data = get_series(series, today, today, settings.BMX_TOKEN)
        print(data)
        if not data:
            log.info("Empty data from Endpoint ")
        #
        for serie in data['bmx']['series']:
            if serie['idSerie'] == settings.BMX_UDI_SERIE:
                Udi.objects.insert_api_data(serie)
            # save dollar
            Dollar.objects.insert_api_data(serie)
