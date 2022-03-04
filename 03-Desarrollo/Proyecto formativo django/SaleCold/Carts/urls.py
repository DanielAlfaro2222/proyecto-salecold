from django.urls import path
from . import views

app_name = 'Carts'

urlpatterns = [
    path('', views.cart_view, name = 'cart'),
    path('add-product/', views.add_product, name = 'add_product'),
    path('remove-product/', views.remove_product, name = 'remove_product'),
]