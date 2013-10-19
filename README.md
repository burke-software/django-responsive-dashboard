django-responsive-dashboard
===========================

A generic and easy dashboard for Django applications.

![screenshot](/images/screen.png)

# Features
- jquery.shapeshift for positioning and ordering
- Per user saving of above
- Stock dashlets - Lists, RSS reader, Admin edit lists, django-report-builder, more to come.
- Add and remove dashlets (not implimented)
- Generic per user configurations on dashlets (not implimented)

## What it can't do
- No ready to use dashboard, you need need for it like contrib.admin.
- Column width is hard coded to 300px with 20px gutters. (Feel free to contribute)

django-responsive-dashboard is a starting point for your dashboard interface. It is not a drop in solution. 
A few dashlets are included, but you probably want to create your own. The included css is VERY minimal,
again you should create your own styling.

# Getting Started

## Installation

1. Install `pip install django-responsive-framework`
2. Add `responsive_dashboard` to INSTALLED_APPS
3. Add `url(r'^', include('responsive_dashboard.urls'))` (I didn't want to add a prefix, but you can if you want)
4. You are done, but it won't do anything yet!
 
## Creating your first dashboard

Create a dashboard.py file in your app's folder. Don't place it in your project folder. Here is a simple example

```
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
```

In my case my app was named sis but you could use anything here. title is optional. Now go to
/sis/optional/dashboard/
And you should see a pretty boring dashboard! 

You probably want more than this. Check out the api reference (eh need create this) or the implimentation 
in [django-sis](https://github.com/burke-software/django-sis/blob/master/ecwsp/sis/dashboards.py)
