from django.utils.translation import ugettext_lazy as _


def hpa_to_mmhg(hpa):
    """
    Convert hectopascal to millimeter of mercury [0 °C]
    """
    return int(hpa / 1.3332239)


def deg_to_compass(num):
    """
    Convert wind bearing angle to compass direction
    """
    val = int((num / 22.5) + .5)
    arr = [_('N'), _('NNE'), _('NE'), _('ENE'), _('E'), _('ESE'), _('SE'), _('SSE'),
           _('S'), _('SSW'), _('SW'), _('WSW'), _('W'), _('WNW'), _('NW'), _('NNW')]
    return arr[(val % 16)]


def format_temperature(temperature, units='C'):
    """
    Format temperature
    """
    t = int(temperature)
    return '{}{} &deg;{}'.format('+' if t > 0 else '', t, units)
