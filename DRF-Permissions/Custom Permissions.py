# ===========================================================
# Create Custom Permissions with use has_permission func
# permissions.py


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_superuser
        )


# ===========================================================
# Create Custom Permissions with use has_object_permission func
# permissions.py


from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user == obj.author.user
        )


# ===========================================================
# Tip : We can create a custom access level that only users who are members of a specific group can access


class isDriver(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='driver').exists()


# ===========================================================