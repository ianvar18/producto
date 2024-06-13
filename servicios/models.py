from django.db import models

# Create your models here.

class Servicio(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    precio = models.CharField(max_length=20)
    foto = models.ImageField(upload_to='servicios')
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre