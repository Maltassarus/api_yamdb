from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsAdminOrSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.is_admin or request.user.is_superuser)
        )


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_moderator
