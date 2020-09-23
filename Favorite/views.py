from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from .models import Favorite


def favListView(request, username):
    if request.method == 'GET':
        user = User.objects.get(username=username)
        favs = Favorite.objects.get(user=user)
        fav_posts = favs.posts.all()

        context = {
            'fav_posts': fav_posts,
        }

        return render(request, 'users/profile.html', context)

    return HttpResponseNotAllowed(['GET'])

