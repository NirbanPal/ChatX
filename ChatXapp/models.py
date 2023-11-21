from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#models for storing the messages


class UserProfileModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True, blank=True)
    online_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username+'->'+str(self.online_status)
    

class ChatModel(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(null=True,blank=True)
    thread_name = models.CharField(null=True,blank=True,max_length=50) #group name
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

class ChatNotification(models.Model):
    chat = models.ForeignKey(ChatModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_seen=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username+str(self.is_seen)
    

