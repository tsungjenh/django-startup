from django.views.generic import View


class BaseView(View):
    SUCCESS_RESPONSE = dict()

    def dispatch(self, request, *args, **kwargs):
        response = super(BaseView, self).dispatch(request, *args, **kwargs)
        if response is None:
            return BaseView.SUCCESS_RESPONSE
        return response
