from django.shortcuts import render
from django.views.generic import  FormView,ListView
from django.urls import reverse_lazy
from .forms import ReservaForm
from .models import Reserva
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ReservaFormView(LoginRequiredMixin,FormView): #LoginRequiredMixin
    template_name='reservas/crear_reserva.html'
    form_class=ReservaForm
    success_url=reverse_lazy('lista_reservas') #redirige a la otra vista
    rol_permitido='mesero'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

class ListaReservasView(LoginRequiredMixin,ListView):
    model=Reserva
    template_name='reservas/lista_reservas.html'
    context_object_name='reservas'
    rol_permitido='admin'