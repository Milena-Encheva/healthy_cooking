from django.urls import path

from healthy_cooking.accounts.views import SignInUserView, SignUpUserView

urlpatterns = (
    path("register/", SignUpUserView.as_view(), name="register"),
    path("login/", SignInUserView.as_view(), name="login"),
)