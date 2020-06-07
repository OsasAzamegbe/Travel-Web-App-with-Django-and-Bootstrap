from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your profile @{username} has been created successfully!')
            return HttpResponseRedirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

