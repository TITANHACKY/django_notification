from django.db.models.signals import post_save
from django.dispatch import receiver
from notification_app.models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Notification)
def send_notification(sender, instance, created, **kwargs):
    """
    Sends a django_notification when a new instance of Notification is created.

    Parameters:
    - sender: The sender of the signal.
    - instance: The instance of Notification that was saved.
    - created: A boolean indicating whether the instance was created or updated.
    """
    if created:
        channel_layer = get_channel_layer()
        group_name = 'django_notification'
        event = {
            'type': 'notify',
            'id': instance.id,
            'title': instance.title,
            'body': instance.body,
            'notification_type': instance.notification_type,
        }
        async_to_sync(channel_layer.group_send)(group_name,event)
