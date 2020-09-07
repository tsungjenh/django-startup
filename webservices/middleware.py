# package
import logging
import json
from datetime import datetime
# django
from django.http import QueryDict
from django.utils.deprecation import MiddlewareMixin
# service
from service.libs.exception import CustomException
from service.django_ext.response import JsonResponse

_LOGGER = logging.getLogger(__name__)


class ApiMiddleware(MiddlewareMixin):
    @staticmethod
    def __process_request_body(request):
        content_type = request.META.get('CONTENT_TYPE')
        body = request.body.decode()
        if content_type.startswith('application/json'):
            request.DATA = json.loads(body) if body else dict()
        elif content_type == 'application/x-www-form-urlencoded':
            request.DATA = request.POST.copy()
        else:
            request.DATA = dict()

    def process_request(self, request):
        request.DATA = QueryDict('')
        if request.method == 'GET':
            request.DATA = request.GET
        else:
            self.__process_request_body(request)

    @staticmethod
    def process_exception(request, exception):
        if isinstance(exception, CustomException):
            response = dict(
                status=exception.error_code.code,
                msg=exception.detail_message,
                timestamp=datetime.now(),
            )
        else:
            response = dict(status=-1, msg='Internal Server Error', timestamp=datetime.now())
        _LOGGER.exception('catched error %s in %s, uid:%s',
                          exception.__class__.__name__, request.path,
                          request.user_id if hasattr(request, 'user_id') else None)
        return JsonResponse(response, status=500)


