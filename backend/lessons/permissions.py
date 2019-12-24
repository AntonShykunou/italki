from rest_framework.permissions import BasePermission
from .choices import PENDING_STATUS, APPROVED_STATUS

class IsApprovedStatus(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.status == PENDING_STATUS
    

class IsDeclinedlStatus(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.status == PENDING_STATUS
    

class IsFinishedlStatus(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.status == APPROVED_STATUS