from django.test import TestCase


class HealthTests(TestCase):
    def test_should_return_ok_when_health_called(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')