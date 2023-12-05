from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfileModel, ChatNotification
import json


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#Signals for Notifications
@receiver(post_save,sender=ChatNotification)
def send_notification(sender,instance,created,**kwargs):
    if created:
        channel_layer = get_channel_layer()
        #unseen messages
        unseenNotifiCounts = ChatNotification.objects.filter(user=instance.user,is_seen=False).count()

        room_gr_name = f"{instance.user.id}_notify"

        data={
            'noOfNotifi':unseenNotifiCounts,
        }
        print(room_gr_name)
    
        async_to_sync(channel_layer.group_send)(
            room_gr_name,
            {
                'type':'send_notification',
                'value':json.dumps(data)
            }

        )


















#signals for offline & online status
@receiver(post_save, sender=UserProfileModel)
def send_onlineStatus(sender,instance,created,**kwargs):

    if not created:
        channel_layer=get_channel_layer()
        #here Instance means the object which will be changing or changed in the UserProfileModel
        user = instance.user.username
        userStatus = instance.online_status

        data={
            'username':user,
            'status':userStatus
        }

        async_to_sync(channel_layer.group_send)(
            'user',
            {
                'type':'send_onlineStatus',
                'value':json.dumps(data)
            }

        )












