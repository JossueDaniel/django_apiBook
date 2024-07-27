from rest_framework import serializers

from book.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento', 'biografia']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['autor', 'titulo', 'genero', 'descripcion', 'fecha_publicacion']
