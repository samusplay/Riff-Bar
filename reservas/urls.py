from django.urls import path
from .views import ReservaFormView, ListaReservasView

urlpatterns = [
    path('reservar/', ReservaFormView.as_view(), name='crear_reserva'),
    path('reservas/', ListaReservasView.as_view(), name='lista_reservas'), #Separar rutas


]
