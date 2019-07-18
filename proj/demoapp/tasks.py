from __future__ import absolute_import, unicode_literals
from proj.celery import app
from django.core.mail import send_mail
from proj import settings


@app.task(bind=True, max_retries=10)
def send_emails_task(self, array_emails, message):
    name = 'CELERY AND DJANGO'
    subject = 'TEST TASK CELERY'
    email_from = settings.EMAIL_HOST_USER
    email_to = array_emails
    message_email = "{}----{}".format(message, name)
    try:
        send_mail(subject,
                  message_email,
                  email_from,
                  email_to,
                  fail_silently=False
                  )
    except Exception as exc:
        raise self.retry(exc=exc, countdown=15)
