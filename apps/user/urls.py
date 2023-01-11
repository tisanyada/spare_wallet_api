from django.urls import path
from . import views


urlpatterns = [
    path("auth/signup", views.signup_viewset, name="signup"),
    path("auth/signin", views.signin_viewset, name="signin"),
    path("auth/me", views.me_viewset, name="me"),
    path("auth/activate_account", views.activate_viewset, name="activate_account"),
]
