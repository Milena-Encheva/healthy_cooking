
from django.urls import path, include
from healthy_cooking.accounts.views import LogInUserView, RegisterUserView, logout_user, ProfileDetailsView

urlpatterns = (
    path("register/", RegisterUserView.as_view(), name="register"),
    path("login/", LogInUserView.as_view(), name="login"),
    path("logout/", logout_user, name='logout'),
    path(
            "profile/<int:pk>/", include([
                path("", ProfileDetailsView.as_view(), name="profile_details"),
            ]),
        )
)
