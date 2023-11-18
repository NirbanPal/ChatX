from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#models for storing the messages

class ChatModel(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField(null=True,blank=True)
    thread_name = models.CharField(null=True,blank=True,max_length=50) #group name
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message