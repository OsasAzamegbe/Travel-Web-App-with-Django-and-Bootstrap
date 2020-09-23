from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from Post.models import Post
from Favorite.models import Favorite

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.request.user == self.get_object().author


def login(request):
    return render(request, 'blog/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your profile  has been created successfully! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'blog/register.html', context)


@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, 'Your profile info has been updated successfully!')
            return redirect(reverse('profile') + f'?page=1&username={ request.user.username }')
    else:
        user = get_object_or_404(User, username=request.GET.get('username'))
        page_num = request.GET.get('page')
        user_update_form = UserUpdateForm(instance=user)
        profile_update_form = ProfileUpdateForm(instance=user.profile)
        fav_posts = user.favorite.posts.all()            

    paginate_by = 5
    posts = Post.objects.filter(author=user)
    paginator = Paginator(posts, paginate_by)
    user_posts = None

    try:
        page_obj = paginator.page(int(page_num))
        user_posts = page_obj.object_list

    except:
        raise Http404("Page does not exist.")

    context = {
        'page_user': user,
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form,
        'user_posts': user_posts,
        'page_obj': page_obj,
        'is_paginated': True,
        'fav_posts': fav_posts,
    }

    return render(request, 'users/profile.html', context)
