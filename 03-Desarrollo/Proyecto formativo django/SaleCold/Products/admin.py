from django.contrib import admin
from .models import Product
from .models import Category
from .models import UnitOfMeasure

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):
    # Se usa para especificar que campos se pintaran en el panel de administracion de django
    list_display = ["name", "unit_price", "stock", "discount", "category"]

    # Se usa para especificar en que campo los datos tendran un link para poder editar el registro de una manera mas sencilla
    list_display_links = ["name"] 

    # Se usa para especificar en que campo los datos se podran editar en la misma lista de registros del panel del admin en django
    list_editable = ["unit_price", "stock", "discount"] 

    # Se usa para crear una barra de busqueda en la cual los registros se filtraran en base al campo o campos que nosotros especifiquemos en este atributo
    search_fields = ["name"] 

    # Se usa para crear un campo de filtro, si especificamos mas de un campo por el cual los registros se filtraran, en el panel aparecera un filtro por cada campo.
    list_filter = ["category"]

    # Se usa para especificar cuantos registros se tendran por pagina, si los registros superan este numero django creara una nueva pagina.
    list_per_page = 12

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin):
    # Se usa para especificar que campos se pintaran en el panel de administracion de django
    list_display = ["name"]

    # Se usa para especificar en que campo los datos tendran un link para poder editar el registro de una manera mas sencilla
    list_display_links = ["name"] 

    # Se usa para crear una barra de busqueda en la cual los registros se filtraran en base al campo o campos que nosotros especifiquemos en este atributo
    search_fields = ["name"] 

    # Se usa para especificar cuantos registros se tendran por pagina, si los registros superan este numero django creara una nueva pagina.
    list_per_page = 12

@admin.register(UnitOfMeasure) 
class UnitOfMeasureAdmin(admin.ModelAdmin):
    # Se usa para especificar que campos se pintaran en el panel de administracion de django
    list_display = ["name"]

    # Se usa para especificar en que campo los datos tendran un link para poder editar el registro de una manera mas sencilla
    list_display_links = ["name"] 

    # Se usa para crear una barra de busqueda en la cual los registros se filtraran en base al campo o campos que nosotros especifiquemos en este atributo
    search_fields = ["name"] 

    # Se usa para especificar cuantos registros se tendran por pagina, si los registros superan este numero django creara una nueva pagina.
    list_per_page = 12