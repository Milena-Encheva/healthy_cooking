from healthy_cooking.accounts.models import CookingUser
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class CookingUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )
