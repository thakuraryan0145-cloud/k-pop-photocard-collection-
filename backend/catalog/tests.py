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
