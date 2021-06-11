"""mydiyblog URL Configuration

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
from django.urls import path, re_path
from django.contrib import admin
import main.views as my_viewes
from django.conf.urls import include, url
from django.contrib.auth.views import auth_logout

urlpatterns = [

    path('admin/', admin.site.urls),
    path(r'', my_viewes.main_page, name='main'),
    re_path(r'^blog/$', my_viewes.post_list, name='index'),
    path(r'blog/<int:pk>/',my_viewes.post_detail, name='article'),
    path('add/', my_viewes.add_post, name='add_post'),
    re_path(r'^login/$', my_viewes.user_login, name='login'),
    re_path(r'^logout',my_viewes.logoutUser, name='logout'),
    re_path(r'^edit/$', my_viewes.edit, name='edit'),
    path('register/', my_viewes.register, name = 'reg'),
    ]