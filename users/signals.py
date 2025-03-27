from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from .utils import send_welcome_email  # Email yuborish funksiyasini chaqiramiz

@receiver(post_save, sender=CustomUser)
def welcome_to_website(sender, instance, created, **kwargs):
    if created and instance.email:
        send_welcome_email(instance.username, instance.email)  # .delay() o‘rniga oddiy funksiya

