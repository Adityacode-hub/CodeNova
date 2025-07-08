# apps/users/urls.py

from django.urls import path
from . import views

urlpatterns = [
   
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('password_change/',views.password_change,name='password_change'),
    path("profile/",views.profile,name='profile'),
]
