from django.urls import path
from api.user.views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView
)
from api.echo.views import EchoView


urlpatterns = [
    # PING
    path('echo/', EchoView.as_view()),
    # USER PROXY PASS TO GO SERVER
    path('user/login/', UserLoginView.as_view()),
    path('user/logout/', UserLogoutView.as_view()),
    path('user/register/', UserRegisterView.as_view()),
]

