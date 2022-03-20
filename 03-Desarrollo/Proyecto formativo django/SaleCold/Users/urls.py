from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('account/', views.dashboardUser, name='dashboard-user'),
    path('update-data-user/', views.updateDataUser, name = "update-data-user"),
    path('contact/', views.contact, name = "contact"),
    path('register/', views.register, name = "register"),
    path('change-password/', views.changePassword, name = 'change-password'),
]