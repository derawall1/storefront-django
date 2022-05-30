from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS

class FullDjangoModelPermission(DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        