from django import forms
from .models import Reserva #Importa el modelo de models.py

class ReservaForm(forms.ModelForm):
    class Meta:
        model=Reserva
        fields='__all__' #usar todos los campos del modelo

    



