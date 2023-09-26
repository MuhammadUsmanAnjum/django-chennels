"""
ASGI config for app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channel_project.settings')
django_asgi_app = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from test_app.routing import ws_urlpatterns


application = ProtocolTypeRouter({
  "http": django_asgi_app,
  'websocket': URLRouter(ws_urlpatterns)
})