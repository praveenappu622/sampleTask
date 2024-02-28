from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import re_path,path
from . import consumers


# application = ProtocolTypeRouter({
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             [
#                 re_path("ws/sentence/", consumers.SentenceConsumer.as_asgi()),
#             ]
#         )
#     ),
# })

websocket_urlpatterns = [
    re_path('ws/sentence/', consumers.SentenceConsumer.as_asgi()),
]