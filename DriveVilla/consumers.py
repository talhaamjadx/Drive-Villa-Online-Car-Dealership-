import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from DriveVilla.models import Thread, ActiveUser
from users.models import CustomUser


class ChannelConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope['user'])
        print("channel websocket connected!")
        print(self.scope)
        username = self.scope['url_route']['kwargs']['user_name']
        self.sender = self.scope['user']
        self.reciepent = CustomUser.objects.get(username=username)
        print(self.sender)
        print(self.reciepent)
        if Thread.objects.filter(sender=self.sender, reciepent=self.reciepent).exists():
            thread = Thread.objects.get(
                sender=self.sender, reciepent=self.reciepent)
        elif Thread.objects.filter(sender=self.reciepent, reciepent=self.sender).exists():
            thread = Thread.objects.get(
                sender=self.reciepent, reciepent=self.sender)
        else:
            thread = Thread.objects.create(
                sender=self.sender, reciepent=self.reciepent)
        self.room_group_name = thread.get_thread_name()
        async_to_sync(self.channel_layer.group_add)(
            'chat_' + self.reciepent.username,
            self.channel_name,
        )
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'get.message',
                'input': text_data_json['input'],
            },
        )
        async_to_sync(self.channel_layer.group_send)(
            'chat_' + self.reciepent.username,
            {
                'type': 'send.message',
                'input': text_data_json['input'],
            },
        )

    def send_message(self, event):
        self.send(text_data=json.dumps({
            'message': event['input']
        }))

    def get_message(self, event):
        self.send(text_data=json.dumps({
            'message': event['input']
        }))


class ThreadConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['url_route']['kwargs']['user_name']
        self.group_name = "chat_" + self.user
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name,
        )
        print(self.group_name)
        self.accept()

    def disconnect(self, code):
        print(code)
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name,
        )

    def receive(self, text_data):
        print(text_data)

    def send_message(self, event):
        self.send(text_data=json.dumps({
            'message': event['input']
        }))


class ActiveComsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'active_users',
            self.channel_name,
        )
        print("works!")
        self.sender = self.scope['user']
        if not ActiveUser.objects.filter(user = self.sender).exists():
            self.active = ActiveUser.objects.create(user = self.sender, status="active")
        text_data_json = {
            "user" : self.sender.username,
            "status": "active",
        }
        text_data_json_string = json.dumps(text_data_json)
        # self.active = Active.objects.create(user = self.sender)
        async_to_sync(self.channel_layer.group_send)(
            'active_users',
            {
                'type': 'send.message',
                'message': text_data_json_string,
            }
        )
        
        self.accept()

    def disconnect(self, code):
        text_data_json = {
            "user" : self.sender.username,
            "status": "inactive",
        }
        text_data_json_string = json.dumps(text_data_json)
        async_to_sync(self.channel_layer.group_send)(
            'active_users',
            {
                'type': 'send.message',
                'message': text_data_json_string,
            }
        )
        print(code)
        async_to_sync(self.channel_layer.group_discard)(
            'active_users',
            self.channel_name,
        )
        self.active = ActiveUser.objects.filter(user = self.sender)
        self.active.delete()

    def send_message(self, event):
        self.send(text_data= event['message'])