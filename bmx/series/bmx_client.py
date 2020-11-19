import logging
import requests
from django.conf import settings

log = logging.getLogger(__name__)


def get_series(series, start_date, end_date, token):
    """ Client for banxico API
        https://www.banxico.org.mx/SieAPIRest/service/swagger-ui.html
    """
    headers = {
        'Accept': 'application/json',
        'Bmx-Token': token,
    }
    id_series = ','.join(series)
    url = settings.BMX_ENDPOINT + \
        f'/v1/series/{id_series}/datos/{start_date}/{end_date}'
    log.debug("Request URL: %s", url)
    response = requests.get(url, headers=headers)
    log.debug("Response code: %s", response.status_code)
    log.debug("Response content: %s", response.text)
    if response.status_code != 200:
        return False
    try:
        return response.json()
    except ValueError as e:
        return {}
