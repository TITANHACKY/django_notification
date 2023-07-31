import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template

class NotificationConsumer(WebsocketConsumer):
    """
    Websocket consumer for handling notifications.
    """
    
    def connect(self):
        """
        Connects the WebSocket consumer to a group in the channel layer.
        """
        self.group_name = 'django_notification'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        """
        Disconnects the WebSocket connection.

        Parameters: close_code (int): The close code to send to the client.
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def notify(self, event):
        """
        Send a django_notification by converting the event to JSON and sending it as text data.

        :param event: The event to be sent as a django_notification.
        :type event: Any
        """
        self.send(text_data=json.dumps(event))