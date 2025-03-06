from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission: 
    - Staff users can ADD, UPDATE, DELETE.
    - Other users can only VIEW.
    """

    def has_permission(self, request, view):
        # SAFE_METHODS are GET, HEAD, OPTIONS (Only Viewing)
        if request.method in permissions.SAFE_METHODS:
            return True  
        
        # Only allow modifications if the user is staff
        return request.user and request.user.is_staff
