from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(username, email):
    subject = "Xush kelibsiz!"
    message = f"Salom {username}, bizning saytga xush kelibsiz!"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
