from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_email_notification(subject, message, recipient_email):
    """
    Отправляет email через Celery.
    """
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient_email],
            fail_silently=False,
        )
        return f"Email sent to {recipient_email}"
    except Exception as e:
        return f"Failed to send email to {recipient_email}: {str(e)}"
