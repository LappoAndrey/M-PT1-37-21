from django.urls import path
from .views import (
    BaseView,
    SmartphoneDetailView,
    NotebookDetailView,
    CartView,
    AddToCartNotebook,
    AddToCartSmartphone,
    DelFromCartNotebook,
    DelFromCartSmartphone,
)
from django.urls.conf import include
import django.contrib.auth.urls as auth_urls


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/smartphones/<str:slug>/', SmartphoneDetailView.as_view(),
         name='smartphones_detail'),
    path('products/notebooks/<str:slug>/', NotebookDetailView.as_view(),
         name='notebooks_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/smartphones/<str:slug>/', AddToCartSmartphone.as_view(),
         name='add_to_cart_smartphone'),
    path('add-to-cart/notebooks/<str:slug>/', AddToCartNotebook.as_view(),
         name='add_to_cart_notebook'),
    path('del-from-cart/smartphones/<str:slug>/',
         DelFromCartSmartphone.as_view(),
         name='del_from_cart_smartphone'),
    path('del-from-cart/notebooks/<str:slug>/',
         DelFromCartNotebook.as_view(),
         name='del_from_cart_notebook'),
    path('accounts/', include(auth_urls))
]
