from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)

    def __Str__(self):
        return f'Author: {self.author}, Title: {self.title}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        width, height = img.size
        
        if width > 1500 and height > 1500:
            img.resize((1500, 1500), Image.LANCZOS)

        img.save(self.image.path)
    
    class Meta:
        ordering = ['date']

