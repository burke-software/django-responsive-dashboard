from django.conf.urls import *
from responsive_dashboard import views, dashboard

dashboard.autodiscover()

urlpatterns = patterns('',
    url('^(?P<app_name>\w+)/dashboard/$',  views.generate_dashboard),
    url('^(?P<app_name>\w+)/dashboard/ajax_reposition/$',  views.ajax_reposition),
    url('^(?P<app_name>\w+)/dashboard/ajax_delete/$',  views.ajax_delete),
    url('^(?P<app_name>\w+)/dashboard/add_dashlet/$',  views.add_dashlet),
    url('^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/$',  views.generate_dashboard),
    url('^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/ajax_reposition/$',  views.ajax_reposition),
    url('^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/ajax_delete/$',  views.ajax_delete),
    url('^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/add_dashlet/$',  views.add_dashlet),
)
