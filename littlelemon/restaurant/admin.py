from django.contrib import admin
from .models import Booking, Menu

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Booking
    """
    list_display = ('Name', 'No_of_guests', 'BookingDate', 'formatted_date')
    list_filter = ('BookingDate', 'No_of_guests')
    search_fields = ('Name',)
    ordering = ('-BookingDate',)
    date_hierarchy = 'BookingDate'
    list_per_page = 20
    
    def formatted_date(self, obj):
        """Muestra la fecha en formato más legible"""
        return obj.BookingDate.strftime('%d/%m/%Y %H:%M')
    formatted_date.short_description = 'Fecha Formateada'
    formatted_date.admin_order_field = 'BookingDate'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Menu
    """
    list_display = ('Title', 'Price', 'Inventory', 'is_available')
    list_filter = ('Price', 'Inventory')
    search_fields = ('Title',)
    ordering = ('Title',)
    list_per_page = 25
    list_editable = ('Price', 'Inventory')
    
    def is_available(self, obj):
        """Indica si el item está disponible basado en el inventario"""
        return obj.Inventory > 0
    is_available.boolean = True
    is_available.short_description = 'Disponible'
    is_available.admin_order_field = 'Inventory'
