import unittest
from django.test import TestCase
from Blog.models import Profile
from Blog.forms import UserRegisterForm
from django.contrib.auth.models import User
import random

class TestUser(unittest.TestCase):
    def setUp(self):
        self.username = self.get_username('TestUserJohnDoe')
        self.data = {'first_name':'John', 'last_name':'Doe', 'username': self.username, 'email': 'johndoe@gmail.com', 'password1':'testing1234', 'password2': 'testing1234'}
        self.user = UserRegisterForm(data=self.data)
        self.user.save()

    def test_user(self):
        exists = User.objects.filter(username=self.data['username']).exists()
        self.assertEqual(exists, True)

        user = User.objects.get(username=self.data['username'])
        self.assertNotEqual(user, None)
        
        user.delete()
        exists = User.objects.filter(username=self.data['username']).exists()
        self.assertEqual(exists, False)


    def get_username(self, username):
        '''
        get unique username
        '''
        exists = User.objects.filter(username=username).exists()
        if exists:
            hashString = self.gen_rand(5)
            return self.get_username(f'{username}_{hashString}')
        return username

    def gen_rand(self, max):
        '''
        generate string of random numbers with length max
        '''
        return ''.join(str(random.randrange(0,10)) for _ in range(max))


class TestProfile(unittest.TestCase):

    def test_add_profile(self):
        profile_size = len(Profile.objects.all())
        user = TestUser()
        user.setUp()
        self.assertEqual(len(Profile.objects.all()), profile_size + 1)
        
        username = user.username
        userObj = User.objects.get(username=username)
        userObj.delete()
        self.assertEqual(len(Profile.objects.all()), profile_size)