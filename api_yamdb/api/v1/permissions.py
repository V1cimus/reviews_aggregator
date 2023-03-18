from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_admin
        )


class IsAdminOrReadOnly(permissions.BasePermission):

    message = "Методы Create, Patch, Delete доступны только админу!"

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
        )


class IsAuthorOrModeratorOrAdminOrReadOnly(permissions.BasePermission):

    message = (
        "Методы Create, Patch, Delete доступны админу, модератору или автору!")

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_admin
            or request.user.is_moderator
            or obj.author == request.user
        )
