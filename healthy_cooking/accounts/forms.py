from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

UserModel = get_user_model()


class CookingUserCreationForm(UserCreationForm):
    """
    A subclass of BaseUserCreationForm where the help_text for password fields is removed.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'about', 'profile_picture']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 4}),
        }
