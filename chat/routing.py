from django.urls import path
from .consumers import ChatConsumers

websocket_urlpatterns = [
    path('ws/<str:room_name>/',ChatConsumers.as_asgi())
]