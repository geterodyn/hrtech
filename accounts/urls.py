from django.urls import path
from .views import LoginView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]