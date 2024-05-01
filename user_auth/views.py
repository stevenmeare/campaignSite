from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('user_auth:registered')
            )
    else:
        form = SignUpForm()
    return render(request, 'authentication/signup.html', {'form':form})
            

def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponseRedirect(
            reverse('user_auth:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('user_auth:show_user')
        )
    
def registered(request):
    return render(request, 'authentication/registered.html')
    
def show_user(request):
    user_info = {}
    print(request.user.username)
    if request.user.is_authenticated:
        user_info["username"] = request.user.username
        # Only access password if user is authenticated
        user_info["password"] = request.user.password
    return render(request, 'authentication/user.html',{
        'user_info':user_info
    })

