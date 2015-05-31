# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DashletSetting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('setting', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='UserDashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dashboard_name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDashlet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dashlet_name', models.CharField(max_length=255)),
                ('position', positions.fields.PositionField(default=-1)),
                ('deleted', models.BooleanField(default=False)),
                ('user_dashboard', models.ForeignKey(to='responsive_dashboard.UserDashboard')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.AddField(
            model_name='dashletsetting',
            name='dashlet',
            field=models.ForeignKey(to='responsive_dashboard.UserDashlet'),
        ),
    ]
