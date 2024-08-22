"""
ASGI config for esbs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esbs.settings')
import django
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.sessions import SessionMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path, re_path

from app.consumers import PushNotificationsConsumer
from middleware.jwt_auth_middleware import JWTAuthMiddleware

from users.models import Users


application = get_asgi_application()

app = ProtocolTypeRouter({
    "http": application,
    "websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            URLRouter([
                path("push-notifications", PushNotificationsConsumer.as_asgi()),
            ])
        )
    ),
})

# Resetting the online counters on server restart
# Note: this is the least ugly option I found to update the DB at startup - it will run 4 times on each startup however
Users.objects.all().update(online=0)