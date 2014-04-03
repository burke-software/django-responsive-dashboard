django-responsive-dashboard
===========================

[![Build Status](https://travis-ci.org/burke-software/django-responsive-dashboard.png?branch=master)](https://travis-ci.org/burke-software/django-responsive-dashboard)

A generic and easy dashboard for Django applications.

# News

Released 1.0. Not feature complete yet - but stable enough to run. Shouldn't need to make any more changes
that break things. Still need to add better documentation and tests.

![screenshot](/images/screen.png)

# Features
- jquery.shapeshift for positioning and ordering
- Per user saving of above
- Stock dashlets - lists, RSS reader, admin edit lists, django-report-builder, more to come
- Add and remove dashlets (not implemented)
- Generic per user configurations on dashlets (not implemented)

## What it can't do
- Not a drop-in dashboard. It needs to be configured, similar to django admin.
- Column width is hard coded to 300px with 20px gutters. (Feel free to contribute.)

django-responsive-dashboard is a starting point for your dashboard interface. It is not a drop in solution. 
A few dashlets are included, but you probably want to create your own. The included CSS is VERY minimal,
again you should create your own styling.

# Documentation

http://django-responsive-dashboard.readthedocs.org
