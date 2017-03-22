from django.conf import settings

api_key = getattr(settings, 'DWD_API_KEY', '')
lang = getattr(settings, 'DWD_LANG', 'en')
