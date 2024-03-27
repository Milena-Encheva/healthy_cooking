from django.contrib.auth.forms import BaseUserCreationForm

from healthy_cooking.accounts.models import CookingUser
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class CustomUserCreationForm(BaseUserCreationForm):
    """
    A subclass of BaseUserCreationForm where the help_text for password fields is removed.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None


class CookingUserCreationForm(auth_forms.UserCreationForm, CustomUserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )



