# chat/routing.py
from django.urls import re_path

from DriveVilla import consumers

websocket_urlpatterns = [
    re_path(r'ws/channel/(?P<user_name>\w+)/$', consumers.ChannelConsumer),
    re_path(r'ws/thread/(?P<user_name>\w+)/$', consumers.ThreadConsumer),
    re_path(r'ws/active/$', consumers.ActiveComsumer),
]
