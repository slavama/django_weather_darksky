from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from jsonfield.fields import JSONField

FORECAST_TYPES = (
    ('currently', _('Currently forecast')),
    ('hourly', _('Hourly forecast')),
    ('daily', _('Daily forecast')),
)


@python_2_unicode_compatible
class WeatherLocation(models.Model):
    """
    Locations
    """
    slug = models.SlugField(_('Slug'), unique=True)
    latitude = models.FloatField(_('Latitude'))
    longitude = models.FloatField(_('Longitude'))
    name = models.CharField(_('Name'), max_length=50)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
        ordering = ['name']

    def __str__(self):
        return '{} ({})'.format(self.name, self.location)

    @property
    def location(self):
        return '{},{}'.format(self.latitude, self.longitude)


@python_2_unicode_compatible
class WeatherForecast(models.Model):
    """
    Forecasts
    """
    location = models.ForeignKey(WeatherLocation, verbose_name=_('Location'))
    forecast_type = models.CharField(_('Type'), choices=FORECAST_TYPES, max_length=30)
    json_data = JSONField(_('JSON data'))
    date_create = models.DateTimeField(_('Date of create'), auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = _('Forecast')
        verbose_name_plural = _('Forecasts')
        ordering = ['-date_create']

    def __str__(self):
        return '{} - {}'.format(self.forecast_type, self.date_create)
