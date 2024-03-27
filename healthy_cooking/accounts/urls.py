from django.urls import path

from healthy_cooking.accounts.views import SignInUserView, SignUpUserView

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("login/", SignInUserView.as_view(), name="login"),
)