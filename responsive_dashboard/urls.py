"""URL patterns."""

from django.conf.urls import url
from responsive_dashboard import views, dashboard

dashboard.autodiscover()

urlpatterns = [  # pylint: disable=invalid-name
    url(r'^(?P<app_name>\w+)/dashboard/$', views.generate_dashboard),
    url(r'^(?P<app_name>\w+)/dashboard/ajax_reposition/$', views.ajax_reposition),
    url(r'^(?P<app_name>\w+)/dashboard/ajax_delete/$', views.ajax_delete),
    url(r'^(?P<app_name>\w+)/dashboard/add_dashlet/$', views.add_dashlet),
    url(r'^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/$', views.generate_dashboard),
    url(r'^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/ajax_reposition/$', views.ajax_reposition),
    url(r'^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/ajax_delete/$', views.ajax_delete),
    url(r'^(?P<app_name>\w+)/(?P<title>\w+)/dashboard/add_dashlet/$', views.add_dashlet),
]
