from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User
from .forms import UserRegisterForm


# Create your views here.


def index(request):
    return render(request, 'index.html')

#
# def login(request):
#     return render(request, 'login.html')


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


def register_user(request):
    post = request.POST
    check = True
    if post:
        if post['firstname']:
            first_name = post['firstname']
        else:
            check = False
            messages.error(request, 'Please enter First Name!')
        if post['lastname']:
            last_name = post['lastname']
        else:
            check = False
            messages.error(request, 'Please enter Last Name!')
        if post['username']:
            username = post['username']
        else:
            check = False
            messages.error(request, 'Please enter Username!')
        if post['email']:
            email = post['email']
        else:
            check = False
            messages.error(request, 'Please enter a valid Email Address!')
        if post['password']:
            password = post['password']
        else:
            check = False
            messages.error(request, 'Please enter a Password!')
        if post['password'] != post['password_confirm']:
            check = False
            messages.error(request, 'Passwords do not match!')
        if check:
            user_exists = User.objects.filter(username=username).exists()
            if not user_exists:
                new_user = User(first_name=first_name, username=username,
                                surname=last_name, email=email, password=password)
                new_user.save()
                messages.success(request, f'Your profile @{username} has been created successfully!')
                return HttpResponseRedirect('/login/')
            else:
                messages.error(request, f'An account with the username: @{username} '
                                        f'already exists. Please choose a new username.')
                return HttpResponseRedirect('/register/')

    return HttpResponseRedirect('/register/')

