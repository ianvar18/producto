from django.db import models

# Create your models here.

class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True)
    categoria = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.categoria)
    
class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    precio = models.CharField(max_length=20)
    barra = models.CharField(max_length=20)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    activo = models.IntegerField()
    def __str__(self):
        return str(self.nombre)