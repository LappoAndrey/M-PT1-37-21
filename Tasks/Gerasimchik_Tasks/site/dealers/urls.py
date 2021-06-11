from django.urls import path
from . import views

urlpatterns = [
    path('add_dealer', views.AddDealer.as_view(), name='add_dealer'),
    path('<slug:slud>/<int:pk>/', views.DealerDetailView.as_view(), name='dealer_detail'),
    path('<slug:slug>/', views.DealersListView.as_view(), name='dealers_by_brand'),
    path('', views.DealersBrandView.as_view(), name='brands_list'),
]
