from django.template.loader import render_to_string
from django.conf import settings
from django.utils.importlib import import_module
from django.db.models.fields import FieldDoesNotExist
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
    template_dict = {}
    require_permissions = ()
    require_apps = ()
    
    def __init__(self, **kwargs):
        title = kwargs.pop('title', None)
        if title:
            self.title=title
        self.template_dict = {
            'title': title
        }
    
    def _render(self):
        return render_to_string(self.template, self.template_dict)

    def __unicode__(self):
        return self._render()
    
    def set_request(self, request):
        """ Set the html request from the view """
        self.request = request

    def _check_perm(self):
        """ Check if user has permission to view """
        for perm in self.require_permissions:
            if not self.request.user.has_perm(perm):
                return False
        return True
    
    def _check_apps(self):
        """ Check if this dashlet has the required apps installed for usage """
        for app in self.require_apps:
            if not app in settings.INSTALLED_APPS:
                return False
        return True

    def allow_usage(self):
        """ Public method to check if the user allowed to use this dashlet """
        if self._check_apps() and self._check_perm():
            return True
        return False

    def is_default(self):
        """ Should this dashlet be shown by default """
        return True


class ListDashlet(Dashlet):
    """ Shows a list of data from a model """
    template = 'responsive_dashboard/list_dashlet.html'
    model = None
    fields = ('__str__',)
    queryset = None
    order_by = ()
    count = 3
    show_change = True
    show_add = False
    show_custom_link = None
    custom_link_text = None
    
    def __init__(self, **kwargs):
        if 'model' in kwargs:
            self.model = kwargs.pop('model', None)
        super(ListDashlet, self).__init__(**kwargs)
    
    def _render(self):
        if self.queryset:
            object_list = self.queryset
        else:
            object_list = self.model.objects.all()
        
        if self.order_by:
            object_list = object_list.order_by(*self.order_by)
        
        object_list = object_list[:self.count]

        results = []
        for obj in object_list:
            result_row = []
            for field in self.fields:
                result_row += [getattr(obj, field)]
            results += [result_row]
        
        headers = []
        for field in self.fields:
            if field == '__str__':
                headers += [self.model._meta.verbose_name]
            else:
                try:
                    if getattr(getattr(self.model, field, None), 'short_description', None):
                        headers += [getattr(getattr(self.model, field), 'short_description')]
                    else:
                        headers += [self.model._meta.get_field(field).verbose_name]
                except FieldDoesNotExist:
                    headers += [field]

        self.template_dict = dict(self.template_dict.items() + {
            'opts': self.model._meta,
            'object_list': object_list,
            'results': results,
            'headers': headers,
            'show_change': self.show_change,
            'show_add': self.show_add,
            'show_custom_link': self.show_custom_link,
            'custom_link_text': self.custom_link_text,
        }.items())
        return super(ListDashlet, self)._render()


class DjangoReportBuilderDashlet(Dashlet):
    """ Shows a report from django-report-builder """



responsive_dashboards = {}
# code from django-admin-tools THANKS!
# https://bitbucket.org/izi/django-admin-tools/src/e2732c0083c76862c7d014b7ab25d0dbd5e467c5/admin_tools/dashboard/registry.py
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
