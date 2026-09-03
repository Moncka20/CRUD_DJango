from django.contrib import admin

from .models import Libro


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'categoria', 'año_publicacion', 'cantidad_disponible')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'autor', 'isbn')
