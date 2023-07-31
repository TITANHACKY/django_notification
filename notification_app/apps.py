from django.apps import AppConfig


class NotificationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notification_app'

    def ready(self):
        """
        Initializes the object and imports the necessary signals from the notification_app module.
        """
        import notification_app.signals
