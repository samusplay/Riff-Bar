from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=100)
    descripcion=models.TextField(blank=True, null=True)
    precio=models.DecimalField(max_digits=8, decimal_places=2)
    categoria=models.CharField(max_length=50,choices=[
        ('comida','Comida'),
        ('debida','Bebida'),
    ])
    stock=models.PositiveIntegerField(default=0)
    disponible=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre