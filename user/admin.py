from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UsersAdmin(UserAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'is_active',
    )

    search_fields = (
        'first_name',
        'last_name',
        'email',
    )

    ordering = ('-id',)
