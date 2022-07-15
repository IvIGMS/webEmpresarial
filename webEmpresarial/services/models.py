from distutils.command.upload import upload
from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitle")
    content = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['-created'] # Aqui podemos usar cualquiera de los campos que tengamos.

    def __str__(self) -> str:
        return self.title