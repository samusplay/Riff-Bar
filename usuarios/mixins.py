# usuarios/mixins.py

from django.contrib.auth.mixins import AccessMixin
from .models import PerfilUsuario

class RolRequiredMixin(AccessMixin):
    rol_permitido = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        try:
            perfil = request.user.perfilusuario
            if perfil.rol != self.rol_permitido:
                return self.handle_no_permission()
        except PerfilUsuario.DoesNotExist:
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)
