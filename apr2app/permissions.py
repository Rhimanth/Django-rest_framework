from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user,"role",None)=="admin"
class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user,"role",None)=="owner"
class IsConsumer(BasePermission):
    def has_permission(self, request, view):
        return getattr(request.user,"role",None)=="consumer"