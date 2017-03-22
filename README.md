Weather wrapper for darksky.net API for Django
==============================================

Install
-------

1) `pip install django_weather_darksky`

2) Add django_weather_darksky to INSTALLED_APPS

3) Add to settings.py
`
# Your API key from https://darksky.net/dev/
DWD_API_KEY = '1234567890'
DWD_LANG = 'ru'
`

4) `python manage.py migrate`

5) Add locations via django admin interface


Usage
-----
1) `python manage.py load_forecast`

2) Add to crontab, for example:
`0/30 * * * * /var/www/SITE/venv/bin/python /var/www/SITE/manage.py load_forecast --currently`
`0 */3 * * * /var/www/SITE/venv/bin/python /var/www/SITE/manage.py load_forecast --daily`

3) Api:

```
from django_weather_darksky import api

api = DarkSkyAPI(API_KEY, 'ru')
api.set_location(56.0083, 92.8706);
print(api.get_forecast())
print(get_currently().temperature)
api.set_location(55.75, 37.6166);
print(get_daily())
```

4) Django:

```
from django import template

from django_weather_darksky.models import WeatherForecast

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

```