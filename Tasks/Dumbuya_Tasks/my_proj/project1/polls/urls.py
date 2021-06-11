from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('selfpage/', views.self, name='self'),
    path('<int:pk>/', views.project_detail, name='project_detail')
]
