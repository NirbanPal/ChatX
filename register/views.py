from django.shortcuts import render

# Create your views here.
from django.contrib.auth  import login
from django.shortcuts import render,redirect
from .forms import SignUpFrom


# Create your views here.

def signup(request):
    if request.method=='POST':
        form=SignUpFrom(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    form=SignUpFrom()
    return render(request,"register/signup.html",{'form':form})