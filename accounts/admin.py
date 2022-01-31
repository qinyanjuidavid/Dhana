from django.contrib import admin
from accounts.models import(User,
                            Administrator, Customer)


@admin.register(User)
class userAdmin(admin.ModelAdmin):
    pass


@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
