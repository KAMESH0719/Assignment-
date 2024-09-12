from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print("Signal received: Saving user...")
    time.sleep(5)  # Simulate a delay in handling
    print(f"User {instance.username} has been saved!")
