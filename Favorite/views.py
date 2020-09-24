from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, Http404
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
def favToggleView(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=pk)
        original_favorites = post.number_of_favorites
        user = request.user
        try:
            favs = user.favorite.posts.all()
            if post in favs:
                post.number_of_favorites -= 1                
                user.favorite.posts.remove(post)
            else:
                post.number_of_favorites += 1
                user.favorite.posts.add(post)

            post.save()
            user.save()

            context = {
                'number_of_favorites': post.number_of_favorites,
            }

            status = 200

        except:
            post.number_of_favorites = original_favorites
            post.save()
            
            context = {}
            status = 500

        return JsonResponse(context, status=status)

    return JsonResponse({"data: method unallowed"}, status=405)