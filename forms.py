from django import forms

# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser # our Custom model


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

