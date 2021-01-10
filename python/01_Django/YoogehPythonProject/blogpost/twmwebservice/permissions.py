from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCustomSatisfied(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username

        if username is not None and username.lower() == 'dba@gmail.com':
            return True
        elif request.method in SAFE_METHODS:
            return True
        else:
            return False
