from django.contrib import admin
from .models import Producto
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'descripcion', 'imagen')
    search_fields = ('nombre', 'descripcion')

admin.site.register(Producto, ProductoAdmin)


