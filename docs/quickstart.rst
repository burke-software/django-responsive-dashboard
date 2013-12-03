.. _quickstart:

Quick Start Guide
=================

Installation
------------

1. Install ``pip install django-responsive-dashboard``
2. Add ``responsive_dashboard`` to INSTALLED_APPS
3. Add ``url(r'^', include('responsive_dashboard.urls'))`` (I didn't want to add a prefix, but you can if you want)
4. Sync your database. You may use South ``./manage.py migrate responsive_dashboard``
5. You are done, but it won't do anything yet!

Creating your first dashboard
-----------------------------

Create a dashboard.py file in your app's folder. Don't place it in your project folder. Here is a simple example ::

    from responsive_dashboard.dashboard import Dashboard, Dashlet

    class ExampleDashlet(Dashlet):
        pass

    class ExampleDashboard(Dashboard):
        app = 'sis'
        title = 'optional'
        dashlets = [
            ExampleDashlet(title="Dashlet Events"),
        ]

    dashboard = ExampleDashboard()

In my case my app was named sis but you could use anything here. title is optional. 
Now go to /sis/optional/dashboard/ And you should see a pretty boring dashboard!

You probably want more than this. 
Check out the api reference (eh need create this) or the implimentation in `django-sis`__

__ https://github.com/burke-software/django-sis/blob/master/ecwsp/sis/dashboards.py
