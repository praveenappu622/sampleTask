"""
ASGI config for interviewTask project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interviewTask.settings')

# application = get_asgi_application()
# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from channels.layers import get_channel_layer
# from django.urls import path
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interviewTask.settings')
# import profiles.routing

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             profiles.routing.application
#         )
#     ),
# })
import os
from django.core.asgi import get_asgi_application
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interviewTask.settings')
 
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from profiles import routing
 
application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() , 
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )    
        )
    }
)
