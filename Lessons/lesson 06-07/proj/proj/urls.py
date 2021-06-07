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

from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', home_views.PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_views.home, name='posts'),
    # path('posts/', home_views.posts, name='posts'),
    # path('posts/add/', home_views.add_post, name='add_post'),
    # path('posts/<int:post_id>/', home_views.post, name='post'),
    # path('posts/<str:query>/', home_views.posts, name='posts'),
    # path('accounts/', include(auth_urls)),
    path('api/v1/', include(router.urls)),
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)