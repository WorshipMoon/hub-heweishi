from django.core.mail import send_mail
from django.conf import settings

def send_order_email(
    subject,
    message,
    recipient_list,
    html_message
):
    subject = subject
    message = message
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = recipient_list
    # send_mail(subject, message, from_email, recipient_list)
    send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=html_message)