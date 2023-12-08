import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import ChatModel,User, UserProfileModel, ChatNotification,Room, Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# @method_decorator(login_required, name='dispatch') 
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
        messageReceiver=data['receiver']

        await self.save_message(messageSender,message,self.room_group_name,messageReceiver)

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
    def save_message(self,sender,message,thread_name,messageReceiver):
        senderObj = User.objects.get(username=sender)
        Chatobj=ChatModel.objects.create(sender=senderObj,message=message,thread_name=thread_name)
        other_user_id=self.scope['url_route']['kwargs']['id']
        receiverObj = User.objects.get(id=other_user_id)
        if messageReceiver == receiverObj.username:
            ChatNotification.objects.create(chat=Chatobj,user=receiverObj)
            # pass

# @method_decorator(login_required, name='dispatch') 
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope['user'].id
        self.room_group_name = f"{user_id}_notify"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def send_notification(self,event):
        data=json.loads(event['value'])
        await self.send(text_data=json.dumps({
            'countOfNotifi':data['noOfNotifi']
        }))






# @method_decorator(login_required, name='dispatch')         
class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'user'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, message):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        username = data['username']
        connection_type = data['type']

        await self.change_online_status(username,connection_type)
    
    async def send_onlineStatus(self,event):
        try:
            data=json.loads(event.get('value'))
            username = data['username']
            online_status = data['status']
            await self.send(text_data=json.dumps({
                'username':username,
                'online_status':online_status
            }))
        except Exception as e:
            print(e)



    @database_sync_to_async
    def change_online_status(self, username, c_type):
        user = User.objects.get(username=username)
        userprofile = UserProfileModel.objects.get(user=user)
        if c_type == "open":
            userprofile.online_status=True
            userprofile.save()
        else:
            userprofile.online_status=False
            userprofile.save()




# rooms websocket and channels
# @method_decorator(login_required, name='dispatch') 
class ChatConsumer(AsyncWebsocketConsumer):
    #function of connecting to the server

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"
        # self.room_group_name = 'chat_%s' % self.room_name

        #join roomname and room group name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # to get the thread id
        # print(threading.get_native_id())

        await self.accept()
        #after this we are authenticated and connected to the server 




    #function of disconnecting the server
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )




    #right code to receive message from websocket
    async def receive(self, text_data):
        # Parse the received JSON message
        message = json.loads(text_data)

        # Extract the message type from the parsed message
        message_type = message['type']

        message_text = message['message']
        message_username = message['username']
        message_room = message['room']

        # Handle different message types
        if message_type == 'chat-message':
            # Handle the chat message
            # await self.handle_chat_message(message)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    # 'type': 'chat.message',(both will work)
                    'message': message_text,
                    'username':message_username,
                    # 'room':message_room
                }
            )

            

            await self.save_message(message_username,message_room,message_text)
        else:
            # Handle other message types or raise an error
            raise ValueError(f"No handler for message type {message_type}")

    #chat_message part
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        # print(event) #it will be printed n times cause it will be sent to all the channels(users) in the group if there is n number of user or channel in the group.

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'username':username
        }))
        




    @database_sync_to_async
    def save_message(self, username, room, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)


        Message.objects.create(user=user, room=room, content=message)
