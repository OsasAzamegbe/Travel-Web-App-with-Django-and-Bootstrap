import unittest
from django.test import Client
from django.urls import reverse

class TestPages(unittest.TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        login = self.client.login(username='AOT', password='Shingeki1997')
        self.assertEqual(login, True)
        self.client.logout()

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
    
    
    def test_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

        login = self.client.login(username='AOT', password='Shingeki1997')
        self.assertEqual(login, True)

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
