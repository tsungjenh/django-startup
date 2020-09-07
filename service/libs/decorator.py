# package
import logging
from datetime import datetime
from functools import wraps
from marshmallow import ValidationError, EXCLUDE
from redis import StrictRedis
# django
from django.conf import settings
from django.http import HttpRequest
# service
from service.const import ResponseStatus
from service.django_ext.response import JsonResponse
from service.libs.exception import (
    CustomException,
    ILLEGAL_PARAMETER,
    ERROR_USER_INVALID_TOKEN
)

_LOGGER = logging.getLogger(__name__)

REDIS = StrictRedis.from_url(settings.USER_REDIS_ADDR, decode_responses=True)


def _wrap2json(data):
    return JsonResponse(dict(status=ResponseStatus.OK.value, msg='', data=data), status=200)


def response_wrapper(func):
    def _wrapper(request, *args, **kwargs):
        try:
            return _wrap2json(func(request, *args, **kwargs))
        except CustomException as why:
            _LOGGER.info('server error! %s %s %s', 500, why or why.detail_message, request.path)
            return JsonResponse(dict(status=ResponseStatus.FAIL.value, msg=why.detail_message,
                                     timestamp=datetime.now()), status=500)
    return _wrapper


def validate_form(schema: object) -> object():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            assert isinstance(request, HttpRequest)
            body = request.DATA
            temp = body.copy()
            for item in temp:
                if item.endswith('[]'):
                    body.update({item[:-2]: body.pop(item)})
            try:
                cleaned_data = schema(unknown=EXCLUDE).load(body)
            except ValidationError as err:
                raise CustomException(ILLEGAL_PARAMETER, err.messages)
            return func(*args, **kwargs, cleaned_data=cleaned_data)
        return wrapper
    return decorator


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        assert isinstance(request, HttpRequest)
        if not request.session.get(settings.SESSION_USER_KEY):
            raise CustomException(ERROR_USER_INVALID_TOKEN)
        else:
            request.user_id = request.session[settings.SESSION_USER_KEY]
            request.session.modified = True
        return func(*args, **kwargs)
    return wrapper



