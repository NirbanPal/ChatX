import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #get the id of the current user (as we are using AuthMiddleWareStack that's why we are geeting the id here)
        my_id = self.scope['user'].id
        other_user_id = self.scope['url_route']['kwargs']['id']
        if int(my_id) > int(other_user_id):
            self.room_name = f'{my_id}-{other_user_id}'
        else:
            self.room_name = f'{other_user_id}-{my_id}'

        self.room_group_name = 'chat_%s' % self.room_name
    
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        ) 

        await self.accept()
        await self.send(text_data=self.room_group_name)
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
