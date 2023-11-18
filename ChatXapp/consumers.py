import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatModel,User

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
        # await self.send(text_data=self.room_group_name)
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        msgType = data['type']
        message=data['message']
        messageSender = data['username']

        if msgType=='chat-message':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type':'chat_message',
                    'message':message,
                    'username':messageSender
                }
            )

            # print(self.room_group_name)
            await self.save_message(messageSender,message,self.room_group_name)

        else:
            raise ValueError(f"No handler for message type {msgType}")

    async def chat_message(self,event):
        message = event['message']
        username = event['username']
        await self.send(text_data=json.dumps({
            'message':message,
            'username':username
        }))

    @database_sync_to_async
    def save_message(self,sender,message,thread_name):
        senderObj = User.objects.get(username=sender)
        ChatModel.objects.create(sender=senderObj,message=message,thread_name=thread_name)
        
