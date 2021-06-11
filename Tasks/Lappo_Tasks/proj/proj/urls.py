"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include
import app.views as home_views
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.urls as auth_urls
from django.contrib.auth import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index, name='index'),
    path('index/', home_views.index, name='index'),

    path('account/home/', home_views.home, name='home'),
    path('account/authorization/', home_views.authorization, name='authorization'),
    path('account/registration/', home_views.registration, name='registration'),


    path('small_wholesale/', home_views.small_wholesale, name='small_wholesale'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)