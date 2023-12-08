from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from ChatXapp.models import ChatModel,Room,Message
from django.contrib.auth.decorators import login_required

User=get_user_model()


# Create your views here.

#All the users except the user logged in as user
@login_required
def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request,'index.html',{'users':users})

#chat page. Here we will get the user is with whom the current user will be chatting
@login_required
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


# views of rooms

@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request,'rooms/rooms.html',{'rooms':rooms})

@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
   

    return render(request, 'rooms/room.html', {'room': room, 'messages': messages})


@login_required
def createrooms(request):

    roomName = request.POST['roomName']
    roomDescription = request.POST['roomDescription']
    if roomName == "" or roomDescription=="":
        return redirect('rooms')
    Room.objects.create(name=roomName,slug=roomName.replace(" ", ""),creator=request.user)
    return redirect('rooms')


