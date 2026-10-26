from django.db import IntegrityError, transaction
from django.db.models import RestrictedError
from django.test import TestCase

from catalog.models import Group, Idol


class CatalogModelTests(TestCase):
    def test_should_reject_duplicate_idol_when_same_group_and_name(self):
        g = Group.objects.create(name='BLACKPINK')
        Idol.objects.create(stage_name='Jennie', group=g)
        with self.assertRaises(IntegrityError), transaction.atomic():
            Idol.objects.create(stage_name='Jennie', group=g)

    def test_should_block_group_delete_when_idols_exist(self):
        g = Group.objects.create(name='BLACKPINK')
        Idol.objects.create(stage_name='Lisa', group=g)
        with self.assertRaises(RestrictedError):
            g.delete()

class SeedFixtureTests(TestCase):
    fixtures = ['seed_groups_idols']

    def test_should_load_3_groups_and_9_idols_when_seed_applied(self):
        self.assertEqual(Group.objects.count(), 3)
        self.assertEqual(Idol.objects.count(), 9)


from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class CatalogApiTests(APITestCase):
    fixtures = ['seed_groups_idols']

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='t@example.com', password='pass12345', display_name='Tester')

    def test_should_reject_when_not_authenticated(self):
        response = self.client.get('/api/groups/')
        self.assertIn(response.status_code, (401, 403))

    def test_should_list_3_groups_when_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get('/api/groups/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 3)

    def test_should_filter_idols_by_group_when_group_given(self):
        self.client.force_authenticate(self.user)
        group = Group.objects.get(name='BLACKPINK')
        response = self.client.get(f'/api/idols/?group={group.group_id}')
        self.assertEqual(response.json()['count'], 3)
