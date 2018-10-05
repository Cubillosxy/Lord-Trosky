import hashlib

from django.conf import settings
from rest_framework import permissions


class ApiPermission(permissions.BasePermission):

    def __init__(self, allowed_methods):
        self.allowed_methods = allowed_methods

    def has_permission(self, request, view):
        api_key = request.META.get('HTTP_API_KEY')
        username = request.user.username
        email = request.user.email
        api_key_user = hashlib.md5('{}-{}-{}'.format(
            username,
            settings.SIGN_API,
            email
        ).encode('utf-8')).hexdigest()
        return all([
            request.method in self.allowed_methods,
            api_key,
            api_key == api_key_user,
        ])
