import requests

API_URL = 'https://api.darksky.net/forecast/{api_key}/{location}'
BLOCKS = ['currently', 'minutely', 'hourly', 'daily', 'alerts', 'flags']


class DarkSkyAPIException(Exception):
    pass


class DarkSkyAPI:
    """
    api = DarkSkyAPI(API_KEY, 'ru')
    api.set_location(56.0083, 92.8706);
    print(api.get_forecast())
    print(get_currently().temperature)
    api.set_location(55.75, 37.6166);
    print(get_daily())
    etc.
    """
    def __init__(self, api_key, lang, units='si'):
        self.api_url = None
        self.api_key = api_key
        self.params = {'lang': lang, 'units': units}

    def set_location(self, latitude, longitude):
        location = '{},{}'.format(latitude, longitude)
        self.api_url = API_URL.format(api_key=self.api_key, location=location)

    def get_forecast(self, element=None):
        if not self.api_url:
            raise DarkSkyAPIException('Location does not set. You need call set_location.')

        response = requests.get(self.api_url, self.params)
        json_data = response.json()

        if element is None:
            return json_data
        elif element in BLOCKS:
            self._set_blocks(element)
            try:
                return json_data[element]
            except KeyError:
                raise DarkSkyAPIException('Response does not contains element {}'.format(element))
        else:
            raise DarkSkyAPIException('Element {} in not correct'.format(element))

    def _set_blocks(self, blocks):
        self.params['exclude'] = ','.join([x for x in BLOCKS if x not in blocks])

    def __getattr__(self, attrname):
        def _call():
            block = (attrname.replace('get_', ''))
            if block in BLOCKS:
                return self.get_forecast(block)
            else:
                raise NameError
        return _call

