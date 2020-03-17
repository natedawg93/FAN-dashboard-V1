from django.urls import path  # new
from channels.auth import AuthMiddlewareStack  # new
from channels.routing import ProtocolTypeRouter, URLRouter  # changed

from dashboard.consumers import DashboardConsumer

# changed
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('index/', DashboardConsumer),
        ])
    )
})