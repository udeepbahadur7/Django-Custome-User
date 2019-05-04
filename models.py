from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# remember to point out AUTH_USER_MODEL in settings.py
# AUTH_USER_MODEL = 'user.CustomUser'
# path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
#     path('register/', user_views.SignUpView.as_view(), name='register'),


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()
