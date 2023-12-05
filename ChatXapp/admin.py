from django.contrib import admin
from ChatXapp.models import ChatModel, UserProfileModel, ChatNotification,Room, Message
# Register your models here.
admin.site.register(ChatModel)
admin.site.register(UserProfileModel)
admin.site.register(ChatNotification)
admin.site.register(Room)
admin.site.register(Message)


