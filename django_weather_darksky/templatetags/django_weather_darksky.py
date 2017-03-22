from django import template

from django_weather_darksky.models import WeatherForecast
from django_weather_darksky.helpers import format_temperature as format_temp

register = template.Library()


@register.inclusion_tag('django_weather_darksky/informer.html', takes_context=True)
def weather_current(context, location):
    """
    Current weather informer
    """
    data = WeatherForecast.objects.filter(location__slug=location, forecast_type='currently').last()
    return {
        'data': data
    }


@register.filter
def format_temperature(value, units='C'):
    """
    Filter format temperature
    """
    try:
        res = format_temp(value, units)
    except ValueError:
        res = ''
    return res
