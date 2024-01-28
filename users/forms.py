from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'surname', 'age', 'sex', 'description', 'email', 'phone', 'avatar', 'country',
                  'city', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('name', 'surname', 'age', 'sex', 'description', 'avatar', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class VerificationCodeForm(forms.Form):
    verification_code = forms.CharField(max_length=6, label='Код верификации')
