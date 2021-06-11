from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.urls as auth_urls

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('login', views.sign_in, name='login'),
    path('create', views.create, name='create'),
    path('register', views.register, name='register'),
    path('log_out', views.log_out, name='log_out'),
    path('profile', views.profile, name="profile"),    
    path('accounts/', include(auth_urls)),
    path('test0', views.test0, name="test0"),
    path('results', views.results, name="results"),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('news/', views.news, name='news'),
    path('news/<int:nnews_id>/', views.nnews, name='nnews'),
    # path('', views.questions, name="home"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

