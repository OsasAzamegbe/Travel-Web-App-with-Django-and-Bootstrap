from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)

    def __Str__(self):
        return f'Author: {self.author}, Title: {self.title}'
    
    class Meta:
        ordering = ['date']

        