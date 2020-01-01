from rest_framework.permissions import BasePermission
from .choices import PENDING_STATUS, APPROVED_STATUS

class CanApproveLessonSession(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.status == PENDING_STATUS
    

class CanDeclinedLessonSession(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.status == PENDING_STATUS
    

class CanFinishLessonSession(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.status == APPROVED_STATUS