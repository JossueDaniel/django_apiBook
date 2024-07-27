from django.db import models


# Create your models here.
class Author(models.Model):
    nombre = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    biografia = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre


class Book(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE, blank=False, null=False)
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=25)
    descripcion = models.TextField(max_length=100)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo

