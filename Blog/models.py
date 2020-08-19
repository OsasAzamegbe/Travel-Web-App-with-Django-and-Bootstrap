from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import pre_save
# from TravelBlog.utils import unique_slug_generator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.user.username} Profile'





# class of objects for various users on the Travel web app
# class User(models.Model):

#     slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
#     first_name = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     surname = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return '%s %s' % ('username:', self.username)


# generates slug for object instances of various classes
# using unique_slug_generator I created in TravelBlog.utils
# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)


# populate the slug field for a User object just before saving into the database
# by calling the slug_generator method.
# pre_save.connect(slug_generator, sender=User)
