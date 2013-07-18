from django.conf.urls.defaults import *
from responsive_dashboard import views

urlpatterns = patterns('',
    url('^(?P<app_name>.+?)/dashboard/$',  views.dashboard),
    url('^(?P<app_name>.+?)/dashboard/ajax_reposition/$',  views.ajax_reposition),
)
