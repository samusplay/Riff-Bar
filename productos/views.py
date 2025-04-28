# productos/views.py
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Producto
from usuarios.models import PerfilUsuario
from django.http import HttpResponseForbidden


# Vista de listar productos
class ListaProductosView(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'productos/lista_productos.html'
    context_object_name = 'productos'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        try:
            perfil = request.user.perfilusuario
            if perfil.rol != 'Administrador':
                return HttpResponseForbidden('No tienes permisos para acceder a esta sección.')
        except PerfilUsuario.DoesNotExist:
            return HttpResponseForbidden('No tienes un perfil asociado.')
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return Producto.objects.all()


        
        

# Vista para crear un producto
class CrearProductoView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = 'productos/crear_producto.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('lista_productos')  # Redirige después de crear

# Vista para editar un producto
class EditarProductoView(LoginRequiredMixin, UpdateView):
    model = Producto
    template_name = 'productos/editar_producto.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('lista_productos')  # Redirige después de editar

# Vista para eliminar un producto
class EliminarProductoView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'productos/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')  # Redirige después de eliminar
