from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import User


# from catalog.models import Product, Version
# from django.forms import inlineformset_factory, BaseInlineFormSet


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar', 'country')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
