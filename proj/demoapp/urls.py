from django.conf.urls import url
from .views import send_emails

urlpatterns = [
    # url que ejecuta la tarea.
    url(r'', send_emails)
]
