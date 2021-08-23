"""SaleCold URL Configuration

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
from . import views

#El . signfica que la libreria que vamos a importar esta dentro de la carpeta de este archivo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('login/', views.login, name = "login"),
    path('administrator/', views.administrator, name = "administrator"),
    path('info/', views.info, name = "info"),
    path('contact/', views.contact, name = "contact"),
    path('register/', views.register, name = "register"),
    path('recuperation/', views.recuperation, name = "recuperation"),
    path('recuperation-phone/', views.recuperationPhone, name = "recuperation-phone"),
    path('recuperation-email/', views.recuperationEmail, name = "recuperation-email"),
    path('change-password/', views.changePassword, name = "change-password"),
    path('confirm-purchase/', views.confirmPurchase, name = "confirm-purchase"),
    path('manage-deliveries/', views.manageDeliveries, name = "manage-deliveries"),
    path('user/', views.userNormal, name = "user-normal"),
    path('add-product/', views.addProduct, name = "add-product"),
    path('update-data-user/', views.updateDataUser, name = "update-data-user")
]

# La funcion path recibe tres parametros, el primer parametro es la url de la ruta, las rutas deben estar en ingles, el segundo parametro llama al archivo views, punto y el nombre de la funcion, y llama a la funcion index, el tercer parametro es un sobrenombre de la funcion, este parametro es opcional
