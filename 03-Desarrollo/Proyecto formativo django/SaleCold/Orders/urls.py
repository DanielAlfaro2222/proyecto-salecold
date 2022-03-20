from django.urls import path
from . import views

app_name = 'Orders'

urlpatterns = [
    path('', views.order_view, name = 'order'),
]