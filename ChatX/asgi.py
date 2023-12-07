"""
ASGI config for ChatX project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatX.settings')

# uvicorn setup
import django
django.setup()


#import part starts here
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

from ChatXapp.consumers import PersonalChatConsumer, OnlineStatusConsumer, NotificationConsumer, ChatConsumer

#import ends here 



application = get_asgi_application()

# added application part starts here

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter([
            path('ws/<int:id>/',PersonalChatConsumer.as_asgi()),
            path('ws/online/',OnlineStatusConsumer.as_asgi()),
            path('ws/notification/',NotificationConsumer.as_asgi()),
            path('ws/<str:room_name>/', ChatConsumer.as_asgi()),
        ])
    )
})
