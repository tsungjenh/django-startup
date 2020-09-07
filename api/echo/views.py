# import package
import logging
# django
from django.utils.decorators import method_decorator
# service
from service.libs.decorator import validate_form, response_wrapper
from service.django_ext.view import BaseView
from .forms import (
    Echo
)
from django.http import HttpResponse

_LOGGER = logging.getLogger(__name__)


class EchoView(BaseView):
    @method_decorator(response_wrapper)
    @method_decorator(validate_form(Echo))
    def get(self, request, cleaned_data):
        return {"echo": cleaned_data}
