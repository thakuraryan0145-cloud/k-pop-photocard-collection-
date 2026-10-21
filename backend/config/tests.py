from django.test import TestCase


class HealthTests(TestCase):
    def test_should_return_ok_when_health_called(self):
        response = self.client.get('/api/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')

from rest_framework.exceptions import NotFound
from rest_framework.test import APIRequestFactory

from config.exceptions import custom_exception_handler


class ExceptionHandlerTests(TestCase):
    def test_should_return_standard_format_when_not_found(self):
        request = APIRequestFactory().get('/api/missing/')
        response = custom_exception_handler(NotFound(), {'request': request})
        self.assertEqual(response.status_code, 404)
        for key in ('timestamp', 'status', 'error', 'message', 'path', 'traceId'):
            self.assertIn(key, response.data)
