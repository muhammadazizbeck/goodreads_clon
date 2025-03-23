from django.core.mail import send_mail
from config.celery import app

@app.task
def send_welcome_email(username, recipient_email):
    subject = "Welcome to Goodreads Clone"
    message = f"Hi {username}, Welcome to Goodreads Clone. Enjoy the books and reviews!"
    sender_email = "aa2004bek@gmail.com"
    
    send_mail(subject, message, sender_email, [recipient_email])