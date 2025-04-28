from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

#Modelo para extender el usuario default
class PerfilUsuario(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    ROL_CHOICES=[
        ('admin','Administrador'),
        ('cajero','Cajero'),
        ('mesero','Mesero'),
    ]
    rol=models.CharField(max_length=10, choices=ROL_CHOICES)

    def __str__(self):
        return f'{self.user.username}-{self.rol}'
