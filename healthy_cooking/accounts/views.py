from audioop import reverse

from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from healthy_cooking.accounts.forms import CookingUserCreationForm, ProfileForm
from django.contrib.auth import views as auth_views, login, logout, get_user_model
from healthy_cooking.accounts.models import Profile


UserModel = get_user_model()

class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class LogInUserView(auth_views.LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class RegisterUserView(views.CreateView):
    template_name = "accounts/register.html"
    form_class = CookingUserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result


def logout_user(request):
    logout(request)
    return redirect('home')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/profile_details.html"


class EditProfileView(OwnerRequiredMixin, views.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/edit_profile.html'
    queryset = Profile.objects.all()

    def get_success_url(self):
        return reverse_lazy('profile_details', kwargs={'pk': self.object.pk})


class DeleteProfileView(views.DeleteView):
    model = UserModel
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()

