from django.db import models
from django.utils.translation import gettext_lazy as _


from .managers import UdiManager, DollarManager

# Create your models here.


class Udi(models.Model):
    date = models.DateField(_('date'))
    value = models.FloatField(_('value'))

    objects = UdiManager()

    class Meta:
        verbose_name = _('udi')
        verbose_name_plural = _('udis')
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'value'], name='udi_date_value_unique')
        ]

    def __str__(self):
        return "%s %s" % (self.date, self.value)


class Dollar(models.Model):
    date = models.DateField(_('date'))
    value = models.FloatField(_('value'))

    objects = DollarManager()

    class Meta:
        verbose_name = _('dollar')
        verbose_name_plural = _('dollars')
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'value'], name='dollar_date_value_unique')
        ]

    def __str__(self):
        return "%s %s" % (self.date, self.value)

# TODO: TIIE
