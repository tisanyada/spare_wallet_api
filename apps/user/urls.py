from django.urls import path
from . import views, auth_views


urlpatterns = [
    path("auth/signup", auth_views.signup_viewset, name="signup"),
    path("auth/signin", auth_views.signin_viewset, name="signin"),
    path("auth/me", auth_views.me_viewset, name="me"),
    path("auth/activate_account", auth_views.activate_viewset, name="activate_account"),
    path("user/home", views.homescreen_viewset, name="home_screen"),
    path("user/wallet", views.walletscreen_viewset, name="wallet_screen"),
]
