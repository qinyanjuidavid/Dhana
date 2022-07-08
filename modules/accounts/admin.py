from django.contrib import admin

from django.contrib.auth.models import Group
from modules.accounts.models import (User, Administrator, Customer)


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', 'username']
    list_display = ("username", "email", "role",
                    "phone", "is_active", "is_admin",
                    "is_staff", "timestamp")
    list_filter = ("is_active", "is_admin", "is_staff", "role")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass
