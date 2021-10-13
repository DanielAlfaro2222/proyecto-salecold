from django.contrib import admin
from .models import TypeOfDelivery
from .models import TypeAccountingDocument
from .models import PaymentType
from .models import HeaderOrdered
from .models import OrderDetail

@admin.register(TypeOfDelivery) 
class TypeOfDeliveryAdmin(admin.ModelAdmin):
    list_display = ["description"]
    list_display_links = ["description"] 
    search_fields = ["description"] 
    list_per_page = 12


@admin.register(TypeAccountingDocument) 
class TypeAccountingDocumentAdmin(admin.ModelAdmin):
    list_display = ["nature"]
    list_display_links = ["nature"] 
    search_fields = ["nature"] 
    list_per_page = 12

@admin.register(PaymentType) 
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ["description"]
    list_display_links = ["description"] 
    search_fields = ["description"] 
    list_per_page = 12

@admin.register(HeaderOrdered) 
class HeaderOrderedAdmin(admin.ModelAdmin):
    list_display = ["order_date", "state", "payment_reference", "type_of_delivery", "type_accounting_document", "payment_type"]
    list_editable = ["state"] 
    search_fields = ["payment_reference"] 
    list_filter = ["type_of_delivery", "type_accounting_document", "payment_type"]
    list_per_page = 12

@admin.register(OrderDetail) 
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ["quantity", "subtotal", "total"]
    list_editable = ["subtotal", "total"] 
    search_fields = ["total", "quantity"] 
    list_filter = ["total"]
    list_per_page = 12