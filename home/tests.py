from django.test import TestCase
from django.urls import reverse




class URLTestsNotLoggedIn(TestCase):
    def test_homapage_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_loginpage(self):
        response = self.client.post(reverse('home:login'), {'username': 'john', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

    def test_contactpage(self):
        response = self.client.get(reverse('home:contact'))
        self.assertEqual(response.status_code, 200)

    def test_membership(self):
        response = self.client.get(reverse('home:membership'))
        self.assertEqual(response.status_code, 200)

class URLTestsLoggedIn(TestCase):

    def test_myprofile(self):
        self.client.login(username='john', password='password')

