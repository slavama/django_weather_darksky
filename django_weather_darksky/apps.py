from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DWDConfig(AppConfig):
    name = 'django_weather_darksky'
    verbose_name = _('Weather Forecasts by darksky.net')
