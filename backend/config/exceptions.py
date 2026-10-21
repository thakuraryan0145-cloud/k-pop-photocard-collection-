import uuid

from django.utils import timezone
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return None

    data = response.data
    message = data.get('detail') if isinstance(data, dict) else None
    request = context.get('request')

    payload = {
        'timestamp': timezone.now().isoformat(),
        'status': response.status_code,
        'error': response.status_text,
        'message': str(message) if message else 'Validation failed',
        'path': request.path if request else '',
        'traceId': str(uuid.uuid4()),
    }
    if message is None:
        payload['errors'] = data
    response.data = payload
    return response
