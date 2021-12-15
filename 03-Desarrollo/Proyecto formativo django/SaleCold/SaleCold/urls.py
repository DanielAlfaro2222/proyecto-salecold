from django.contrib import admin
from django.urls import path
from . import views
from Users import views as views_users
from django.conf import settings
from django.conf.urls.static import static
from Products import views as views_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "index"),
    path('login/', views_users.login_view, name = "login"),
    path('logout/', views_users.logout_view, name = "logout"),
    path('administrator/', views_users.administrator, name = "administrator"),
    path('info/', views.info, name = "info"),
    path('contact/', views_users.contact, name = "contact"),
    path('register/', views_users.register, name = "register"),
    path('recuperation/', views_users.recuperation, name = "recuperation"),
    path('recuperation-phone/', views_users.recuperationPhone, name = "recuperation-phone"),
    path('recuperation-email/', views_users.recuperationEmail, name = "recuperation-email"),
    path('change-password/', views_users.changePassword, name = "change-password"),
    path('confirm-purchase/', views.confirmPurchase, name = "confirm-purchase"),
    path('manage-deliveries/', views.manageDeliveries, name = "manage-deliveries"),
    path('add-product/', views.addProduct, name = "add-product"),
    path('update-data-user/', views_users.updateDataUser, name = "update-data-user"),
    path('product/<slug:slug>', views_products.ProductDetailView.as_view(), name='product'),
    path('panel-user/', views_users.panelUser, name='panel-user'),
    path('category/<slug:slug>', views_products.CategoryDetailView.as_view(), name='category'),
    path('search/', views_products.ProductSearchListView.as_view(), name='search'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)