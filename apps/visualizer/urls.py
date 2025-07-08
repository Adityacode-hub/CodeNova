from django.urls import path
from . import views
urlpatterns = [
    path('', views.visualizer, name='users-visualizer'),
]