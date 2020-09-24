from django.shortcuts import render
from django.views.generic import ListView
from Post.models import Post


class TrendingListView(ListView):
    model = Post
    ordering = ['-number_of_favorites']
    context_object_name = 'posts'
    paginate_by = 5
