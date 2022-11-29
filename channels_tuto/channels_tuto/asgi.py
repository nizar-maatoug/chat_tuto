"""
ASGI config for channels_tuto project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channels_tuto.settings')
django_asgi_app=get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    #add other protocols
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
    ),
})
