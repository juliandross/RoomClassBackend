
from rest_framework.permissions import BasePermission

class IsCoordinator(BasePermission):
    """
    Permite el acceso solo a usuarios con rol COORDINADOR.
    """
    def has_permission(self, request, view):
        print("Checking if user is coordinator")
        print(f"User role: {getattr(request.user, 'rol', None)}")
        return hasattr(request.user, 'rol') and request.user.rol == 'COORDINADOR'