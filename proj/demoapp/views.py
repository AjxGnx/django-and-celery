from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_emails_task


# Vista que llama a la tarea.
def send_emails(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        send_emails_task.delay([request.POST['array_emails']], request.POST['message'])
        return HttpResponse('Emails sended using Celery')
