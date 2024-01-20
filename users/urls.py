from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, activate, email_activate, restore_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('activate/<str:uid>/', activate, name="activate"),
    path('email_activate', email_activate, name="email_activate"),
    path('restore_password', restore_password, name="restore_password")
]