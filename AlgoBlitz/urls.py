"""
URL configuration for AlgoBlitz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from apps.users import views 


urlpatterns = [
    path('', views.home, name='user-home'),
    path('admin/', admin.site.urls),
    path('users/',include('apps.users.urls')),
    path('submissions/',include('apps.submissions.urls')),
    path('streaks/',include('apps.streaks.urls')),
    path('problems/',include('apps.problems.urls')),
    path('visualizer/',include('apps.visualizer.urls')),
    # path('accounts/',include('apps.accounts.urls')),
    path('achievement/', include('apps.achievements.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)