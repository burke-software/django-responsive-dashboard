from django.shortcuts import render_to_response
from responsive_dashboard.dashboard import *

def dashboard(request, app_name="", title=""):
    dashboard = responsive_dashboards['{0}__{1}'.format(app_name, title)]
    
    return render_to_response(dashboard.template, {'dashboard': dashboard})
