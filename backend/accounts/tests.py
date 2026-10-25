from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from catalog.models import Group

from .models import User


class RegisterTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("register")
        self.valid = {
            "email": "new@example.com",
            "password": "Strong#Pass2026",
            "display_name": "New User",
        }

    def test_should_create_user_when_data_valid(self):
        response = self.client.post(self.url, self.valid, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(email="new@example.com").exists())

    def test_should_not_return_password_when_registered(self):
        response = self.client.post(self.url, self.valid, format="json")
        self.assertNotIn("password", response.data)

    def test_should_hash_password_when_saved(self):
        self.client.post(self.url, self.valid, format="json")
        user = User.objects.get(email="new@example.com")
        self.assertNotEqual(user.password, "Strong#Pass2026")
        self.assertTrue(user.check_password("Strong#Pass2026"))

    def test_should_reject_duplicate_email(self):
        self.client.post(self.url, self.valid, format="json")
        response = self.client.post(self.url, self.valid, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data["errors"])

    def test_should_reject_weak_password(self):
        data = {**self.valid, "password": "123"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("password", response.data["errors"])

    def test_should_reject_missing_display_name(self):
        data = {"email": "a@example.com", "password": "Strong#Pass2026"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 400)

    def test_should_save_favorite_group_when_given(self):
        group = Group.objects.create(name="TWICE")
        data = {**self.valid, "favorite_group": str(group.pk)}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, 201)
        user = User.objects.get(email="new@example.com")
        self.assertEqual(user.favorite_group, group)