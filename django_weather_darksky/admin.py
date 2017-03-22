from django.contrib import admin

from .models import WeatherLocation, WeatherForecast


class WeatherLocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(WeatherLocation, WeatherLocationAdmin)


class WeatherForecastAdmin(admin.ModelAdmin):
    pass

admin.site.register(WeatherForecast, WeatherForecastAdmin)
