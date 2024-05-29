from rest_framework import permissions

class adminPermission(permissions.BasePermission):
    # admin is allowed to create things
    
    def has_permission(self, request, view):
        if request.method == "POST" and request.user.is_superuser:
            return True
        elif request.method == "PUT" and request.user.is_superuser:
            return True
        elif request.method == "DELETE" and request.user.is_superuser:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True

        return False
