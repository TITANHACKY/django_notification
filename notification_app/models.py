from django.db import models


class Notification(models.Model):
    """
    Represents a django_notification.

    Attributes:
        title (str): The title of the django_notification.
        body (str): The body content of the django_notification.
        notification_type (str): The type of the django_notification.
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    notification_type = models.CharField(max_length=50)
