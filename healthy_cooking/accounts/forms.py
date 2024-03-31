from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

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
