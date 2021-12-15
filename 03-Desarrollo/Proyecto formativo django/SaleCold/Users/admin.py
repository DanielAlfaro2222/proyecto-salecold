from django.contrib import admin
from .models import UserModel
from .models import City
from .models import TypeOfDocument
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Contact

@admin.register(City) 
class CityAdmin(admin.ModelAdmin):
    list_display = ["description", "zip_code"]
    list_display_links = ["description"] 
    search_fields = ["description", "zip_code"] 
    list_per_page = 18

@admin.register(TypeOfDocument) 
class TypeOfDocumentAdmin(admin.ModelAdmin):
    list_display = ["description"]
    list_display_links = ["description"] 

@admin.register(UserModel) 
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'type_of_document', 'number_document', 'gender', 'city', 'phone_number']
    # Buscar por los campos de la clase User de django
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name'] 
    list_per_page = 18

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

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'subject', 'first_name', 'last_name', 'phone_number', 'email']
    search_fields = ['ticket', 'first_name', 'last_name', 'email'] 
    list_per_page = 18

    fieldsets = (
        ("Informacion de contacto", {
            'fields': ('first_name', 'last_name', 'phone_number', 'email', )
        }), ("Mensaje", {
            'fields': ('subject', 'message', )
        })
    )