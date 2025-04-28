# productos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.CrearProductoView.as_view(), name='crear_producto'),
    path('listar/', views.ListaProductosView.as_view(), name='lista_productos'),
    path('editar/<int:pk>/', views.EditarProductoView.as_view(), name='editar_producto'),
    path('eliminar/<int:pk>/', views.EliminarProductoView.as_view(), name='eliminar_producto'),
]

