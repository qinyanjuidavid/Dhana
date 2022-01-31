from django.db.models.signals import (post_save,)
from accounts.models import User, Customer, Administrator
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_users(sender, instance, created, *args, **kwargs):
    if created:
        if (instance.role == "administrator"
            or instance.is_admin or
                instance.is_staff):
            Administrator.objects.update_or_create(
                user=instance
            )

        elif (instance.role == "customer"):
            Customer.objects.update_or_create(
                user=instance
            )
