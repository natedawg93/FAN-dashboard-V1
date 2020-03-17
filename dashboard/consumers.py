from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from django.db.models.signals import post_save
from django.dispatch import receiver

from .serializers import ButtonSerializer
from .models import Button

import json


class DashboardConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.group_name = ''

    async def connect(self):
        self.group_name = 'button_created'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
    
    # async def receive_json(self, content, **kwargs):
    #     # message_type = content.get('type')
    #     # if message_type == 'create.button':
    #     await self.send_data(content)

    # @receiver(post_save, sender=Button)
    async def button_created_message(self, event):
        # button = await self._send_data(event.get('data'))
        # button_data = ButtonSerializer(button).data
        # await self.send_json({
        #     'type': 'create.button',
        #     'data': button_data
        # })'
        await self.send(text_data='created')
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('button_created', self.channel_name)

    @database_sync_to_async
    def _send_data(self, content):
        serializer = ButtonSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        data = serializer.create(serializer.validated_data)
        print(data)
        return data