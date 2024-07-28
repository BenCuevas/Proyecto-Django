from django.contrib import admin
from .models import Producto, Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","stock"]
    list_editable = ["precio", "stock"]
    search_fields = ["nombre"]
    list_per_page = 5

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)