from tkinter import CASCADE
from django.db import models
from django.utils.timezone import now # Lo necesitamos para el campo 'published'
from django.contrib.auth.models import User

"""
Vamos a crear dos modelos, el de categoria con post es N:M y el de post con usuarios
es 1:N.
"""

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created'] # Aqui podemos usar cualquiera de los campos que tengamos.


    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    # Este campo sirve para poner manualmente una fecha, pero por defeco va a salir la actual.
    published = models.DateTimeField(verbose_name="Fecha de publicacion", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created'] # Aqui podemos usar cualquiera de los campos que tengamos.


    def __str__(self) -> str:
        return self.title