from django.template.loader import render_to_string
from django.conf import settings
from django.utils.importlib import import_module
import imp

class Dashboard(object):
    """ Base class for dashboards
    """

    title = ''
    app = ''
    template = 'responsive_dashboard/dashboard.html'

    def __init__(self):
        responsive_dashboards['{0}__{1}'.format(self.app, self.title)] = self


class Dashlet(object):
    """ Base class for dashlets
    """
    title = None
    template = 'responsive_dashboard/dashlet.html'
    
    def __init__(self, title=None):
        if title:
            self.title=title

    def __unicode__(self):
        html = render_to_string(self.template, {
            'title': self.title,
            })
        return html


responsive_dashboards = {}
for app in settings.INSTALLED_APPS:
    # try to import the app
    try:
        app_path = import_module(app).__path__
    except AttributeError:
        continue

    # try to find a app.dashboard module
    try:
        imp.find_module('dashboards', app_path)
    except ImportError:
        continue

    # looks like we found it so import it !
    import_module('%s.dashboards' % app)
