from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm


admin.site.register(CustomUser, CustomUserAdmin)

