from django.urls import path
from . import views
urlpatterns = [
    path('', views.accounts, name='users-accounts'),
]