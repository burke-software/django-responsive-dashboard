from django.db import models
from positions.fields import PositionField


class UserDashboard(models.Model):
    """ Settings for a dashboard for one user
    """
    dashboard_name = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User')


class UserDashlet(models.Model):
    """ One dashlet for one user
    """
    user_dashboard = models.ForeignKey(UserDashboard)
    dashlet_name = models.CharField(max_length=255)
    position = PositionField(collection='user_dashboard')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('position',)


class DashletSetting(models.Model):
    """ One setting for a user's dashlet
    """
    dashlet = models.ForeignKey(UserDashlet)
    setting = models.CharField(max_length=255)
    value = models.CharField(max_length=2048)
