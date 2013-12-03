django-responsive-dashboard
===========================

[![Build Status](https://travis-ci.org/burke-software/django-responsive-dashboard.png?branch=master)](https://travis-ci.org/burke-software/django-responsive-dashboard)

A generic and easy dashboard for Django applications.

# News

Made some potentially incompatible [changes](https://github.com/burke-software/django-responsive-dashboard/commit/741481cbc25a41588c34d369393f8d0ee1f16663) to dashlets. 
Hoping to release 1.0 soon with some documentation. Won't be making such drastic changes afer 1.0.

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

# Documentation

http://django-responsive-dashboard.readthedocs.org
