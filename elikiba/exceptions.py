from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError
from rest_framework.exceptions import AuthenticationFailed
from django.core.exceptions import ValidationError as DjangoValidationError

from .errors import CustomError  # Import your custom error class


def elikiba_exception_handler(exc, context):
    if isinstance(exc, CustomError):
        # Handle the custom error and create a custom response
        custom_response = {
            "error": str(exc)
        }
        return Response(custom_response, status=exc.status_code)

    # Check if the exception is a validation error
    if isinstance(exc, ValidationError):
        # Handle validation errors and create a custom response
        custom_response = {
            "error": "Validation error",
            "details": exc.detail
        }
        return Response(custom_response, status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, DjangoValidationError):
        error_messages = []
        for field, errors in exc.message_dict.items():
            error_messages.extend([f"{field}: {error}" for error in errors])
        custom_response = {
            "error": "Validation error",
            "details": error_messages
        }
        return Response(custom_response, status=status.HTTP_400_BAD_REQUEST)

    if isinstance(exc, AuthenticationFailed):
        custom_response = {
            "error": exc.detail,
        }
        return Response(custom_response, status=status.HTTP_401_UNAUTHORIZED)

    # For other exceptions, use the default exception handler
    response = exception_handler(exc, context)

    if response is not None and 'non_field_errors' in response.data:
        # Modify the response format
        custom_response = {
            "error": response.data['non_field_errors'][0]
            if response.data['non_field_errors'] else "An error occurred"
        }
        response.data = custom_response

    return response
