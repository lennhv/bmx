import logging
import datetime
from django.db import models
from django.utils import timezone
from django.db.utils import IntegrityError


log = logging.getLogger(__name__)


def _str_to_date(s):
    return datetime.datetime.strptime(s, '%d/%m/%Y')


def _save_data(model, serie):
    for value in serie['datos']:
        date = _str_to_date(value['fecha'])
        ins = model(date=date, value=float(value['dato']))
        try:
            ins.save()
        except IntegrityError:
            pass


class UdiManager(models.Manager):

    def insert_api_data(self, serie):
        """ 
        """
        _save_data(self.model, serie)
        return


class DollarManager(models.Manager):

    def insert_api_data(self, serie):
        """ 
        """
        _save_data(self.model, serie)
        return
