from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction
from django.db.utils import OperationalError

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    try:
        # Attempt to create another user as part of the same transaction
        User.objects.create(username='signaluser')
    except OperationalError:
        print("Database operation failed in the signal handler!")
