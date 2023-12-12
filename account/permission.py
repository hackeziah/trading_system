from rest_framework.permissions import BasePermission


class IsSuperUserUser(BasePermission):
    """
    Allows access only to superuser users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)