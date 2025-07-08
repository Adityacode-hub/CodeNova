from django.urls import path
from . import views

urlpatterns = [
    path('', views.submissions, name='users-submissions'),
]
