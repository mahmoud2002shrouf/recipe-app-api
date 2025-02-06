

"""
test for mode;
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test user model with email and password."""

    def test_create_user_with_email_and_password(self):
        """test create user with email and password."""

        email = "test@example.com"
        password = "testpassword123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_ucer_with_email_normailz(self):
        """test email for user is normalized"""
        email_sample = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['TEST2@EXAMPLE.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]
        for eamil, expected in email_sample:
            user = get_user_model().objects.create_user(eamil, 'sample123')
            self.assertEqual(user.email, expected)
