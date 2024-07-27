from django.contrib import admin
from .models import Book, Author


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'autor', 'genero', 'fecha_publicacion']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'nacionalidad', 'fecha_nacimiento']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
