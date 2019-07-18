from __future__ import absolute_import, unicode_literals
from proj.celery import app

from celery.schedules import crontab
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


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(200, test_task.s('test'), )

    sender.add_periodic_task(
        crontab(hour=19, minute=1, day_of_week=4),
        coffee_task.s(),
    )


@app.task(bind=True, max_retries=10)
def coffee_task(self):
    name = 'BMKeros R.L'
    subject = 'COFFEE ALERT'
    message = 'son las 3, quien se va a hacer el cafe? hablen claro... TAREA PROGRAMADA CELERY-DJANGO...'
    email_from = settings.EMAIL_HOST_USER
    email_to = ['alirio1925@gmail.com''hostelixisrael@gmail.com', 'antonycarrizo96@gmail.com', 'juancho199217@gmail',
                'jesusnavas2210@gmail.com ', 'ivantelix@gmail.com']
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


@app.task
def test_task(arg):
    print(arg)
