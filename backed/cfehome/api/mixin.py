from rest_framework import permissions

from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permissions_class = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
        permissions.AllowAny
    ]

