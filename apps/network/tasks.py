from celery import shared_task

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives

from .models import Subscriber, Post, Log


@shared_task
def notify_new_content_async(post_id):
    """
    Sending and email.
    :param post_id: Post id.
    """
    post = Post.objects.get(id=post_id)
    subscribers = Subscriber.objects.all()
    for subscriber in subscribers:
        print(f'Enviando email de nuevo contenido a... {subscriber.full_name}')
        html_content = f"¡Hola {subscriber.full_name}! Te informamos que tenemos " \
                       f"un nuevo contenido: <b>{post.title}<b>"
        msg = EmailMultiAlternatives("¡Nuevo contenido!", html_content, 'from@example.com', [subscriber.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        log = Log(sent_to=subscriber.email, data=html_content)
        log.save()


@shared_task
def notify_new_subscriber_async(subscriber_id):
    """
    Sending and email.
    :param subscriber_id: Subscriber id
    """
    subscriber = Subscriber.objects.get(id=subscriber_id)
    staffs = User.objects.filter(is_staff=True)
    for user in staffs:
        html_content = f"¡Hola {user.first_name}! Te informamos se "\
                       f"registró una nueva persona:" \
                       f"<p><b>Nombre:</b> {subscriber.full_name}<br> " \
                       f"<b>Email:</b> {subscriber.email}</p>"
        msg = EmailMultiAlternatives("¡Nuevo suscriptor!", html_content, 'from@example.com', [user.email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        log = Log(sent_to=user.email, data=html_content)
        log.save()
