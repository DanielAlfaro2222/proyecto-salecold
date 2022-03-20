from django.contrib import admin
from .models import UserModel
from .models import City
from .models import TypeOfDocument
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

@admin.register(City) 
class CityAdmin(admin.ModelAdmin):
    list_display = ["description", "zip_code", "modified", "state"]
    list_display_links = ["description"] 
    search_fields = ["description", "zip_code"] 
    list_per_page = 10

@admin.register(TypeOfDocument) 
class TypeOfDocumentAdmin(admin.ModelAdmin):
    list_display = ["description", "modified", "state"]
    list_display_links = ["description"] 

@admin.register(UserModel) 
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'type_of_document', 'number_document', 'gender', 'city', 'phone_number']
    # Buscar por los campos de la clase User de django
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name'] 
    list_per_page = 10

    fieldsets = (
        ("Informacion adicional del usuario",{
            'fields': ('user', 'type_of_document', 'number_document', 'gender', 'address', 'city', 'phone_number',)
        }),
    )

class UserInline(admin.StackedInline):
    model = UserModel
    can_delete = False 
    verbose_name_plural = 'Usuarios'

class UserDjangoAdmin(UserAdmin):
    inlines = (UserInline,)

admin.site.unregister(User)
admin.site.register(User, UserDjangoAdmin)