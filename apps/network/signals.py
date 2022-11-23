from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post, Subscriber
from .tasks import notify_new_content_async, notify_new_subscriber_async


@receiver(post_save, sender=Post)
def send_mail_to_subscriber(sender, **kwargs):
    """
    Sending message to subscribers when exist a new post.
    When a post is created
    """
    if kwargs.get('created', False):
        post = kwargs.get("instance")
        notify_new_content_async.delay(post.id)


@receiver(post_save, sender=Subscriber)
def new_subscriber(sender, **kwargs):
    """
    Sending message staff when exist a new subscriber.
    """
    if kwargs.get('created', False):
        subscriber = kwargs.get("instance")
        notify_new_subscriber_async.delay(subscriber.id)
