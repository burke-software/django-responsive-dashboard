from django.conf.urls.defaults import *
from responsive_dashboard import views

urlpatterns = patterns('',
    url('^(?P<app_name>.+?)/dashboard/$',  views.generate_dashboard),
    url('^(?P<app_name>.+?)/dashboard/ajax_reposition/$',  views.ajax_reposition),
    url('^(?P<app_name>.+?)/dashboard/ajax_delete/$',  views.ajax_delete),
    url('^(?P<app_name>.+?)/dashboard/add_dashlet/$',  views.add_dashlet),
)
