from rest_framework import permissions
class Userpermission(permissions.BasePermission):   
    """
    Here,Custom permission class created used to give our own permissions.
    """
    edit_methods = ("PUT", "PATCH")
    def has_object_permission(self, request,view, obj):
            
        if request.user.is_superuser:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        elif obj == request.user:
            return True
        elif obj==request.is_superuser:
            return True
        else:
            return False
        
class UserListPermission(permissions.BasePermission):
        """
        Here,Custom permission class created used to give our own permissions.
        """ 

        def has_permission(self, request, view):
           if request.user.is_superuser:
                return True

        def has_object_permission(self, request,view,obj):
          
            if request.user.is_superuser:
                return True
            else:
                return False
           