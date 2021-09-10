from django.test import TestCase

from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_sucess(self):
        """Test creating a new user with an email is successful"""
        email = 'test@foobar.com'
        password = 'superSecret'

        user = get_user_model().objects.create_user(
                email=email,
                password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test the email for new user is normalized"""
        email = 'test@FOOBAR.CoM'
        user = get_user_model().objects.create_user(email, 'slkfj')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test user with no email raises error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'slkfj')

    def test_create_superuser(self):
        """Test creating a new superuser"""

        user = get_user_model().objects.create_superuser(
            'super@user.com',
            'password'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
