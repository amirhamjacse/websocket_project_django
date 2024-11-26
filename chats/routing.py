from django.urls import path
from chats.consumer import ChatConsumer

websocket_urlpatterns = [
    # path('ws/chat/', ChatConsumer.as_asgi()),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]
