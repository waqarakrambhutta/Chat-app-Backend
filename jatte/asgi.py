import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE','jatte.settings')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jatte.settings')

django_asgi_application = get_asgi_application()

application =  ProtocolTypeRouter(
    {
        'http':django_asgi_application,
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        )
    }
)