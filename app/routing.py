from django.urls import path

from app.consumers import PushNotificationsConsumer


websocket_urlpatterns = [
    path(r'push-notifications', PushNotificationsConsumer.as_asgi()),
]