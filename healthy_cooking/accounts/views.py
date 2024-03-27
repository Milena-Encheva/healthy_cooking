from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from healthy_cooking.accounts.forms import CookingUserCreationForm
from django.contrib.auth import views as auth_views, login, logout


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = "accounts/register.html"
    form_class = CookingUserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result
