from rest_framework.permissions import BasePermission

class IsApprovedStatus(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.status == 'pending':
            return False
    
class IsDeclinedlStatus(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.status == 'pending':
                return True
        return False
    
class IsFinishedlStatus(BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.status == 'approved':
            return True
        return False