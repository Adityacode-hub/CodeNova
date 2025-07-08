from django.urls import path
from . import views
urlpatterns = [
    path('', views.streaks, name='users-streaks'),
]