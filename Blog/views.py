from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def register_user(request):

    post = request.POST
    check = True
    # if post['username'] != '':
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
                messages.success(request, f'@{username}\'s profile has been created successfully!')
                return HttpResponseRedirect('/login/')
            else:
                messages.error(request, f'An account with the username: @{username} '
                                        f'already exists. Please choose a new username.')
                return HttpResponseRedirect('/register/')

    return HttpResponseRedirect('/register/')

    # empty_fields = ""
    # for item in post:
    #     if post[item] == '':
    #         empty_fields += item + ", "
    # if empty_fields:
    #     register(request, empty_fields)
    #     return HttpResponseRedirect('/register/')
