from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def mainView(request):
    return render(request=request, template_name='index.html', context={})

def homeView(request):
    source = uploadVideo.objects.all()
    return render(request=request, template_name='home.html', context={'sourceVideo': source})

def exception_handling(request, exception):
    return render(request, 'exception.html', {})

# LOG IN | SING IN 
def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(uesrname=username, password=password)
            login(request, user)
            messages.success(request, ('Your Registration is SUCCESSFUL'))
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'registerUser.html', context )


def loginUser(request):
    return render(request=request, template_name='loginUser.html', context={})