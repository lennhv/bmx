from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Udi(models.Model):
    date = models.DateField(_('date'))
    value = models.FloatField(_('value'))

    class Meta:
        verbose_name = _('udi')
        verbose_name_plural = _('udis')

    def __str__(self):
        return self.value


class Dollar(models.Model):
    date = models.DateField(_('date'))
    value = models.FloatField(_('value'))

    class Meta:
        verbose_name = _('dollar')
        verbose_name_plural = _('dollars')

    def __str__(self):
        return self.value

# TODO: TIIE
