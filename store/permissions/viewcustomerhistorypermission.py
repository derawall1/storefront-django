from rest_framework.permissions import BasePermission, SAFE_METHODS

class ViewCustomerHistoryPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('store.view_history')
        