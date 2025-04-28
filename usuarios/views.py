from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from usuarios.models import PerfilUsuario

# Vista para registrar un nuevo usuario
def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado exitosamente.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/registro.html', {'form': form})


# Vista para iniciar sesión
def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Aquí traemos el perfil  de admin, cajero,mesero
            try:
                perfil = PerfilUsuario.objects.get(user=user)
                request.user.perfilusuario = perfil
            except PerfilUsuario.DoesNotExist:
                messages.error(request, 'El usuario no tiene un perfil asociado.')
                return redirect('login')

            messages.success(request, f'Bienvenido {user.username}')
            return redirect('lista_productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})


# Vista para cerrar sesión
def logout_usuario(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente.')
    return redirect('login')

