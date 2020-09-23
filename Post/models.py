from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    number_of_favorites = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f'Author: {self.author}, Title: {self.title}'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if self.image:
    #         img = Image.open(self.image.path)
    #         width, height = img.size
            
    #         if width > 1000 and height > 1000:
    #             img.resize((1000, 1000), Image.LANCZOS)

    #         img.save(self.image.path)
        
    class Meta:
        ordering = ['-date']



