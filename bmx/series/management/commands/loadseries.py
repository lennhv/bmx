import datetime
from django.utils import timezone
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.utils.translation import gettext_lazy as _


from series.models import Udi, Dollar
from series.bmx_client import get_series


class Command(BaseCommand):
    help = 'Load series for the first time from Banxico API'

    def add_arguments(self, parser):
        # parser.add_argument('series', type=str)
        parser.add_argument('start-date', type=str,
                            help=_('search start date into API'))
        parser.add_argument('end-date', type=str,
                            help=_('search end date into API'))

    def handle(self, *args, **options):
        series = [settings.BMX_UDI_SERIE,
                  settings.BMX_DOLLAR_SERIE]
        data = get_series(series, options['start-date'],
                          options['end-date'], settings.BMX_TOKEN)
        if not data:
            self.stdout.write(self.style.SUCCESS(
                'Not found data for series in the date range'))
        # 
        for serie in data['bmx']['series']:
            self.stdout.write(self.style.SUCCESS(serie))
            if serie['idSerie'] == settings.BMX_UDI_SERIE:
                Udi.objects.insert_api_data(serie)
                continue
            # save dollar
            Dollar.objects.insert_api_data(serie)
        self.stdout.write(self.style.SUCCESS('Success'))
