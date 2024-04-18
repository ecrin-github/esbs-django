"""
ASGI config for esbs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.sessions import SessionMiddlewareStack
from django.core.asgi import get_asgi_application

import app.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esbs.settings')

application = get_asgi_application()

app = ProtocolTypeRouter({
    "http": application,
    "websocket": AllowedHostsOriginValidator(
        SessionMiddlewareStack(
            URLRouter(app.routing.websocket_urlpatterns)
        )
    ),
})
