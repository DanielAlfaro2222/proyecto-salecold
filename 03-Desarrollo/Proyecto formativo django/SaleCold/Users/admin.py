from django.contrib import admin
from .models import User
from .models import City
from .models import TypeOfDocument

@admin.register(User) 
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email", "city", "address"]
    list_display_links = ["username"] 
    search_fields = ["first_name", "last_name", "email"] 
    list_filter = ["is_staff", "is_active"]
    list_per_page = 12

@admin.register(City) 
class CityAdmin(admin.ModelAdmin):
    list_display = ["description", "zip_code"]
    list_display_links = ["description"] 
    search_fields = ["description", "zip_code"] 
    list_filter = ["description"]
    list_per_page = 12

@admin.register(TypeOfDocument) 
class TypeOfDocumentAdmin(admin.ModelAdmin):
    list_display = ["description"]
    list_display_links = ["description"] 