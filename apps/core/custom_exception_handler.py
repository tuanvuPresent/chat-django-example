import logging

from rest_framework.exceptions import APIException, ErrorDetail
from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.core.constants import ErrorMessage
from apps.core.base_response import CustomResponse


def custom_exception_handler(exc, context):
    logger = logging.getLogger(str(context['view']))
    response = exception_handler(exc, context)
    exc_class = exc.__class__.__name__
    if response is not None:
        status_code = response.status_code
        detail = None
        if exc_class == 'ValidationError':
            error = ErrorMessage.UNKNOWN_ERROR
            detail = get_full_errors_messages(response.data)
        elif exc_class == "CustomAPIException":
            error = exc.detail
        elif exc_class == "AuthenticationFailed":
            error = ErrorMessage.INVALID_AUTH
        elif exc_class == "NotAuthenticated":
            error = ErrorMessage.NOT_AUTH
        elif exc_class == "PermissionDenied":
            error = ErrorMessage.NOT_PERMISSION
        elif exc_class == "Throttled":
            error = ErrorMessage.THROTTLED_REQUEST
        elif exc_class == "Http404":
            error = ErrorMessage.NOT_FOUND
        elif exc_class == "MethodNotAllowed":
            error = ErrorMessage.NOT_ALLOW_METHOD
        else:
            error = ErrorMessage.UNKNOWN_ERROR
            detail = str(exc)

    else:
        detail = str(exc)
        error = ErrorMessage.UNKNOWN_ERROR
        status_code = 500

        logger.error(exc)

    return Response(
        data=CustomResponse(
            status=False,
            code=error.code,
            message=error.message,
            data=detail
        ).data,
        status=status_code
    )


def get_errors_code(detail):
    if isinstance(detail, list):
        for item in detail:
            if item:
                return get_errors_code(item)
    elif isinstance(detail, dict):
        for key, value in detail.items():
            return '{}_{}'.format(key, get_errors_code(value))
    elif isinstance(detail, ErrorDetail):
        return detail.code


def get_full_errors(detail):
    if isinstance(detail, list):
        errors = [get_full_errors(item) for item in detail if item]
        if len(errors) > 1:
            return errors
        return errors[0]
    elif isinstance(detail, dict):
        return {key: get_full_errors(value) for key, value in detail.items()}
    return {
        'message': detail,
        'code': detail.code
    }


def get_full_errors_codes(detail):
    if isinstance(detail, list):
        errors = [get_full_errors_codes(item) for item in detail if item]
        if len(errors) > 1:
            return errors
        return errors[0]
    elif isinstance(detail, dict):
        return {key: get_full_errors_codes(value) for key, value in detail.items()}
    return detail.code


def get_full_errors_messages(detail):
    if isinstance(detail, list):
        errors = [get_full_errors_messages(item) for item in detail if item]
        if len(errors) > 1:
            return errors
        return errors[0]
    elif isinstance(detail, dict):
        return {key: get_full_errors_messages(value) for key, value in detail.items()}
    return detail


class CustomAPIException(APIException):
    status_code = 400

    def __init__(self, message=None, code=None):
        self.code = code
        self.detail = message
