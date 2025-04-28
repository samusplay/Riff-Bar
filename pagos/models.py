from django.db import models

# Create your models here.

class Pago(models.Model):
    #mesa= models.Charfield(max_length=10)# Comentario sprint4
    monto=models.DecimalField(max_digits=10, decimal_places=2)

    METODOS_PAGO=[
        ('efectivo','Efectivo'),
        ('datafono','Datafono'),
        ('qr','QR'),
    ]
    metodo_pago=models.CharField(max_length=10, choices=METODOS_PAGO)
    fecha_pago=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pago de {self.monto}por {self.metodo_pago}'
    