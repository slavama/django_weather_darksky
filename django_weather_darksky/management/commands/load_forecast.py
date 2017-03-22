import time
from django.core.management.base import BaseCommand
from django.db import transaction

from django_weather_darksky.settings import api_key, lang
from django_weather_darksky.api import DarkSkyAPI
from django_weather_darksky.models import WeatherLocation, WeatherForecast


class Command(BaseCommand):
    """
    Usage:
    python manage.py load_forecast --type currently
    python manage.py load_forecast --type daily --clear CLEAR
    """
    @transaction.atomic
    def load_forecast(self, clear, tp):
        if clear:
            WeatherForecast.objects.filter(forecast_type=tp).delete()

        api = DarkSkyAPI(api_key, lang)

        for loc in WeatherLocation.objects.all():
            api.set_location(loc.latitude, loc.longitude)
            data = api.get_forecast(tp)
            WeatherForecast(location=loc, forecast_type=tp, json_data=data).save(force_insert=True)
            time.sleep(2)

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            default=False,
            help='Delete old data')

        parser.add_argument(
            '--type',
            default='currently',
            help='Limit of records for load')

    def handle(self, *args, **options):
        self.load_forecast(options['clear'], options['type'])
