from django.urls import path, include
from django.contrib import admin
from accounts import views as v
import django.contrib.auth.urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notebook.urls')),
    path('register/', v.register, name='register'),
    path('accounts/', include(auth_urls))
]
