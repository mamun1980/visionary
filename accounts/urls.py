from django.urls import path, include
from .views import UserLoginView, UserRegistrationView, profile, logout_view


urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path('profile/', profile, name='profile')
]
