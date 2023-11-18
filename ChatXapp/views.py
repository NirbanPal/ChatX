from django.shortcuts import render
from django.contrib.auth import get_user_model
from ChatXapp.models import ChatModel

User=get_user_model()


# Create your views here.

#All the users except the user logged in as user
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request,'index.html',{'users':users})

#chat page. Here we will get the user is with whom the current user will be chatting
def chatPage(request,username):
    # user_obj is that object with whom the currect user will talk
    user_obj = User.objects.get(username=username)
    users = User.objects.exclude(username=request.user.username)

    if request.user.id > user_obj.id:
        threadName = f"chat_{request.user.id}-{user_obj.id}"
    else:
        threadName = f"chat_{user_obj.id}-{request.user.id}"

    messages = ChatModel.objects.filter(thread_name=threadName)

    return render(request,'main_chat.html',{'users':users,'user':user_obj,'messages':messages})
