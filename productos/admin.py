from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "precio",
        "stock",
        "activo",
        "fecha_creacion",
    )

    search_fields = (
        "codigo",
        "nombre",
    )

    list_filter = (
        "activo",
    )