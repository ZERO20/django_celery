from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Post, Subscriber


class Index(ListView):
    model = Post
    paginate_by = 100
    template_name = "index.html"


class CreateSubscriber(CreateView):
    model = Subscriber
    fields = "__all__"
    success_url = "/"
    template_name = "index.html"

    def get_success_url(self):
        message = '<b>¡Yei!</b> Ahora recibirás por email todas las actualizaciones de nuestro contenido :D'
        messages.success(self.request, message=message)
        return reverse('network:index')
