from django.contrib import admin
from .models import UserModel
from .models import City
from .models import TypeOfDocument
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

@admin.register(UserModel) 
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'type_of_document', 'gender', 'city']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user_last_name'] 
    list_filter = ['city', 'type_of_document']
    list_per_page = 15

    fieldsets = (
        ("Informacion del usuario",{
            'fields': ('user', 'type_of_document', 'number_document', 'gender', 'address', 'city', 'phone_number',)
        }),
    )

class UserInline(admin.StackedInline):
    model = UserModel
    can_delete = False 
    verbose_name_plural = 'Usuarios'

class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

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
