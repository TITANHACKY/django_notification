from django.urls import path
from notification_app import views
from notification_app import consumers

urlpatterns = [
    path('', views.home, name='home'),
]

websocket_urlpatterns = [
    path('ws/notifications', consumers.NotificationConsumer.as_asgi()),
]