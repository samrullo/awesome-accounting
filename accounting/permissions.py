from rest_framework import permissions
from .models import Teacher,Child,Parent
import logging

logger=logging.getLogger(__name__)

class IsBusinessAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the admin role in any business
        return request.user.business_users.filter(role='admin').exists()

class TeacherAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a teacher
        return (
            Teacher.objects.filter(user_id=request.user.id).exists()
            and request.method in permissions.SAFE_METHODS            
        ) or request.user.business_users.filter(role='admin').exists()

    def has_object_permission(self, request, view, obj):
        is_admin=request.user.business_users.filter(role='admin').exists()
        # Allow teachers to view other teachers, children, and parents, but not edit them
        if isinstance(obj, (Teacher, Child, Parent)):
            return  (Teacher.objects.filter(user_id=request.user.id).exists() and request.method in permissions.SAFE_METHODS) or is_admin
        return is_admin
