from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from .dashboard import dashboards
from .models import UserDashboard, UserDashlet


@login_required
def generate_dashboard(request, app_name="", title=""):
    """ Generate a dashboard view by looking up the dashboard from its name
    responsive_dashboards is a list of all possible dashboards """
    dashboard_name = app_name
    if title:
        dashboard += "__{}".format(title)
    dashboard = dashboards.get_dashboard(dashboard_name)

    user_dashboard = UserDashboard.objects.get_or_create(
        dashboard_name=dashboard_name,
        user=request.user,
        )[0]
    user_dashlets = user_dashboard.userdashlet_set.all()
    dashlet_names = []
    addable_dashlet_names = []
    for dashlet in dashboard.dashlets:
        dashlet.set_request(request)
        if (dashlet.is_default() and
            not user_dashlets.filter(dashlet_name=dashlet.title)):
            user_dashlets.create(dashlet_name=dashlet.title, user_dashboard=user_dashboard)
        dashlet_names += [dashlet.title]
        if dashlet.allow_multiple or user_dashlets.filter(deleted=False, dashlet_name=dashlet.title).count() == 0:
            addable_dashlet_names += [dashlet.title]
    user_dashlets = user_dashlets.filter(
        dashlet_name__in=dashlet_names,
        deleted=False,)
    for user_dashlet in user_dashlets:
        for dashlet in dashboard.dashlets:
            if dashlet.title == user_dashlet.dashlet_name:
                dashlet.user_dashlet = user_dashlet # Lets us access per user settings in templates
                user_dashlet.dashlet = dashlet
                break
    include_jquery = False
    if getattr(settings, 'RESPONSIVE_DASHBOARD_INCLUDE_JQUERY', None) == True:
        include_jquery = True
    return render(request, dashboard.template_name, {
        'dashboard': dashboard,
        'dashlets': user_dashlets,
        'new_dashlet_names': addable_dashlet_names,
        'app_name': app_name,
        'title': title,
        'include_jquery': include_jquery
    })


@login_required
def ajax_reposition(request, app_name="", title=""):
    """ Save the position field in the user dashlet
    django-positions should take care of everythign """
    dashlet = UserDashlet.objects.get(
        user_dashboard__user=request.user, id=request.POST['dashlet_id'])
    dashlet.position = int(request.POST['position'])
    dashlet.save()
    return HttpResponse('SUCCESS')


@login_required
def ajax_delete(request, app_name="", title=""):
    """ Delete user dashlet by marking as deleted. """
    dashlet = UserDashlet.objects.get(
        user_dashboard__user=request.user, id=request.POST['dashlet_id'])
    dashlet.deleted = True
    dashlet.save()
    return HttpResponse('SUCCESS')


@login_required
def add_dashlet(request, app_name="", title=""):
    """ Add a new user dashlet then reload the page """
    dashboard_name = '{0}__{1}'.format(app_name, title)
    dashboard = dashboards.get_dashboard(dashboard_name)
    user_dashboard = UserDashboard.objects.get_or_create(
        dashboard_name=dashboard_name,
        user=request.user,
        )[0]

    dashlet_name = request.GET['dashlet_name']
    if not dashlet_name:
        raise Exception('Cannot add a null dashlet')

    UserDashlet.objects.create(
        user_dashboard=user_dashboard,
        dashlet_name=dashlet_name,
    )
    return redirect(request.META['HTTP_REFERER'])
