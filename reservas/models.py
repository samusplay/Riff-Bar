from django.db import models

# Create your models here.
class Reserva(models.Model):
    numero_mesa=models.IntegerField()
    nombre_cliente=models.CharField(max_length=100)
    estado=models.CharField(max_length=20,choices=[('libre', 'Libre'),('reservada','Reservada'),('ocupada','Ocupada')])
    fecha_hora=models.DateTimeField()
    foto=models.ImageField(upload_to="imagenes",null=True,blank=True,verbose_name="foto")

    def __str__(self):
        return f"Mesa {self.numero_mesa} esta {self.estado}para {self.nombre_cliente}"

