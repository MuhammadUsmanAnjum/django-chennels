from django.urls import path
from .consumer import MySyncConsumer


ws_urlpatterns = [
    path('ws/test/', MySyncConsumer.as_asgi())
]