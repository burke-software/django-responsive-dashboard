"""
Test most of the bundled Dashlets.
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.test import TestCase, override_settings

from responsive_dashboard.dashboard import LinksListDashlet, Dashboard, dashboards, AdminListDashlet, ListDashlet
from responsive_dashboard.views import generate_dashboard


urlpatterns = [  # pylint: disable=invalid-name
    url(r'^', include('responsive_dashboard.urls')),
    url(r'^$', generate_dashboard, {'app_name': 'tests'}),
    url('admin/', admin.site.urls),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # ... some options here ...
        },
    },
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


@override_settings(ROOT_URLCONF=__name__)
@override_settings(TEMPLATES=TEMPLATES)
@override_settings(TEMPLATES=INSTALLED_APPS)
class SimpleTest(TestCase):
    """Simple test case."""

    def setUp(self):
        super(SimpleTest, self).setUp()
        self.user = User.objects.create_user(username='testuser', email='none@nowhere.none', password='12345')
        self.user.is_superuser = True
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_link_list(self):
        """
        Tests that example.com was in the dashboard.
        """
        response = self.client.get('/tests/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "example.com")

    def test_admin_list(self):
        """
        Tests that the admin list found the User and Group admins
        """
        response = self.client.get('/tests/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="/admin/auth/group/">Group</a>', html=True)
        self.assertContains(response, '<a href="/admin/auth/user/">User</a>', html=True)

    def test_user_list(self):
        """
        Tests that the testuser was found.
        """
        response = self.client.get('/tests/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser', html=True)
        self.assertContains(response, 'none@nowhere.none', html=True)


class UserListDashlet(ListDashlet):
    """Sample model list dashlet."""
    model = User
    fields = ('username', 'email', 'is_superuser')
    columns = 2
    count = 8
    require_permissions_or = ('admin.change_user', 'admin.view_user')
    order_by = ('-id',)


class TestDashboard(Dashboard):
    """Sample dashboard."""
    app = 'tests'
    title = "Tests"
    dashlets = [
        AdminListDashlet(title="User Management", app_label="auth"),
        UserListDashlet(title="User List"),
        LinksListDashlet(title="Links")
    ]


dashboards.register('tests', TestDashboard)
