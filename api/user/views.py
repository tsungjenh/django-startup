# import package
import logging
# django
from django.utils.decorators import method_decorator
from django.conf import settings
# service
from service.libs.decorator import validate_form, response_wrapper
from service.django_ext.view import BaseView
from service.biz.user import handler
from .forms import (
    UserLoginForm,
    UserRegisterForm
)

_LOGGER = logging.getLogger(__name__)


class UserLoginView(BaseView):
    @method_decorator(response_wrapper)
    @method_decorator(validate_form(UserLoginForm))
    def post(self, request, cleaned_data):
        user = handler.login(**cleaned_data)
        print(user)
        request.session[settings.SESSION_KEY] = user['id']
        return {}


class UserRegisterView(BaseView):
    @method_decorator(response_wrapper)
    @method_decorator(validate_form(UserRegisterForm))
    def post(self, request, cleaned_data):
        return handler.register(**cleaned_data)


class UserLogoutView(BaseView):
    @method_decorator(response_wrapper)
    def post(self, request):
        try:
            del request.session[settings.SESSION_KEY]
        except KeyError:
            pass
        return dict()

