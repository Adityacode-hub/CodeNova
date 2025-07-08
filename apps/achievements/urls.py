from django.urls import path
from .import views
urlpatterns=[
    path('',views.acheivement,name='user-acheivement')
    ]