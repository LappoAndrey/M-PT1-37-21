"""project URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path
import app.views as home_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
import django.contrib.auth.urls as auth_urls

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('', home_views.home, name='home'),
    path('add_article', home_views.add_article, name='add_article'),
    path('blog', home_views.blog, name='blog'),
    path('<int:article_id>/', home_views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', home_views.leave_comment, name='leave_comment'),
    path('accounts/', include(auth_urls)),
    path('register/', home_views.register, name='register'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)