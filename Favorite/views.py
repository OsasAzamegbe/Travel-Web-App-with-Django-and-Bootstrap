from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, JsonResponse
from django.contrib.auth.decorators import login_required  
from .models import Favorite
from Post.models import Post


# def favListView(request, username):
#     if request.method == 'GET':
#         user = User.objects.get(username=username)
#         favs = Favorite.objects.get(user=user)
#         fav_posts = favs.posts.all()

#         context = {
#             'fav_posts': fav_posts,
#         }

#         return render(request, 'users/profile.html', context)

#     return HttpResponseNotAllowed(['GET'])

@login_required
def favAddView(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=pk)
        user = request.user

        if post.number_of_favorites:
            post.number_of_favorites += 1
        else:
            post.number_of_favorites = 1
            
        user.favorites.add(post)
        post.save()
        user.save()
        context = {
            'number_of_favorites': post.number_of_favorites,
        }
        return JsonResponse(context)

    return HttpResponseNotAllowed(['GET'])

