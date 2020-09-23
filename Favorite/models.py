from django.db import models
from django.contrib.auth.models import User
from Post.models import Post


class Favorite(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, related_name='favorites', blank=True)

    def __str__(self):
        return f"{self.user.username}'s favorites"