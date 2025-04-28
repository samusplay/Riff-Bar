from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model=Pago
        fields=['monto','metodo_pago']# Agrega 'mesa' sprint 4