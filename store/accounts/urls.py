from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path("login/",  auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("logout/confirm/", TemplateView.as_view(template_name="accounts/logout_confirm.html"), name="logout_confirm"),
]
