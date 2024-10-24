from django.contrib import admin
from django.urls import path, include
from .views import index,signup,logout_view,redirect_login

urlpatterns = [
    path("", index, name="index"),
    path("index", index, name="index"),
    path("signup", signup, name="signup"),
    path("logout", logout_view, name="logout"),
    path("redirect_login/", redirect_login, name="redirect_login"),
]
