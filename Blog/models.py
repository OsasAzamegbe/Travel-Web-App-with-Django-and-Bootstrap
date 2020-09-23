from django.db import models
from django.contrib.auth.models import User
# from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.user.username} Profile'


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)
    #     width, height = img.width, img.height

    #     if height > 250 and width > 250:
    #         img.thumbnail((250, 250))        
    #         img.save(self.image.path)



