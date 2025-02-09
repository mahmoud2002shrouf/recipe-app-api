"""
test admin
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTets(TestCase):
    """test django admin"""

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            name="testuser",
            password="password123"
        )

    def test_user_list(self):
        """test user list on page"""
        urls = reverse("admin:core_user_changelist")
        res = self.client.get(urls)
        print(self.user.email)
        self.assertContains(res, self.user.email)
        self.assertContains(res, self.user.name)

    def test_edit_user_page(self):
        urls = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(urls)
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works."""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
