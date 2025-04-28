from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Pago
from .forms import PagoForm
from django.urls import reverse_lazy
# Create your views here.

class CrearPagoView(CreateView):
    model=Pago
    form_class=PagoForm
    template_name='pagos/crear_pago.html'
    success_url=reverse_lazy('crear_pago')

    