from rest_framework import permissions
import logging

logger=logging.getLogger(__name__)

class IsBusinessAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user has the admin role in any business
        return request.user.businessuser_set.filter(role='admin').exists()
