"""TravelBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from Blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.PostListView.as_view(), name='index'),
    path('post/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', blog_views.PostEditView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', blog_views.register, name='register'),
    path('map/', include('map.urls')),
    path('accounts/', include('Blog.urls')),
    path('favorite/', include('Favorite.urls')),
    path('post/', include('Post.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
