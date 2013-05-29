from django.shortcuts import render
from responsive_dashboard.dashboard import *
from responsive_dashboard.models import UserDashboard

def dashboard(request, app_name="", title=""):
    dashboard_name = '{0}__{1}'.format(app_name, title)
    dashboard = responsive_dashboards[dashboard_name]
    
    user_dashboard = UserDashboard.objects.get_or_create(
        dashboard_name=dashboard_name,
        user=request.user,
        )[0]
    user_dashlets = user_dashboard.userdashlet_set.all()
    dashlet_names = []
    for dashlet in dashboard.dashlets:
        dashlet.set_request(request)
        if (dashlet.is_default() and 
            not user_dashlets.filter(dashlet_name=dashlet.title)):
            user_dashlets.create(dashlet_name=dashlet.title, user_dashboard=user_dashboard)
        dashlet_names += [dashlet.title]
    user_dashlets = user_dashlets.filter(
        dashlet_name__in=dashlet_names, 
        deleted=False,)
    for user_dashlet in user_dashlets:
        for dashlet in dashboard.dashlets:
            if dashlet.title == user_dashlet.dashlet_name:
                user_dashlet.dashlet = dashlet
                break
    include_jquery = False
    if getattr(settings, 'RESPONSIVE_DASHBOARD_INCLUDE_JQUERY', None) == True:
       include_jquery = True
    return render(request, dashboard.template, {
        'dashboard': dashboard,
        'dashlets': user_dashlets,
        'include_jquery': include_jquery
    })
