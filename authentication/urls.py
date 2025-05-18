# -*- coding: utf-8 -*-
from django.urls import path
from .views import LoginView, LogoutView, SignupView, UserDetailView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth-login'),
    path('auth/logout/', LogoutView.as_view(), name='auth-logout'),
    path('auth/signup/', SignupView.as_view(), name='auth-signup'),
    path('auth/user-detail/', UserDetailView.as_view(), name='auth-user-detail'),
]
