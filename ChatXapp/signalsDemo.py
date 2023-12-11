from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfileModel
import json


from channels.layers import get_channel_layer
#as our web socket functions are async function thats why we need this
from asgiref.sync import async_to_sync

#receiver decorator(what kind of signal, who will be the sender). Here receiver is invoking the signal(post_save signal). Means if there is any cahnges in the UserprofileModel this function will be triggred.

@receiver(post_save, sender=UserProfileModel)
def sendOnlineStatus(sender,instance,created,**kwargs):
    #created will be true when our object will be created for the very fast time. But here we are interested about the value change of the online_status attribute which is by default false. So value of the online_status won't be changing when the object is created. Thats why we are insterested when the object/value will be updated
    if not created:
        channel_layer=get_channel_layer()
        print(channel_layer)
        # as our sender is UserProfileModel so the value which is updated is our instance. so if we do instance.user.username we will get the username of the particular sender ehose status is updated.
        user = instance.user.username
        userStatus = instance.online_status

        data={
            'username':user,
            'status':userStatus
        }

        async_to_sync(channel_layer.group_send(
            'user',{
                'type':'send_onlineStatus',
                'value':json.dumps(data)
            }

        ))





