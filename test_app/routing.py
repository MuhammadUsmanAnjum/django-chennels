from django.urls import path
from .consumer import MySyncConsumer


ws_urlpatterns = [
    path('ws/test/<str:name>/', MySyncConsumer.as_asgi())
]