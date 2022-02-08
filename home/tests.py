from django.test import TestCase
from django.urls import reverse




class URLTestsNotLoggedIn(TestCase):
    def test_homapage_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_loginpage(self):
        response = self.client.get(reverse('home:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_contactpage(self):
        response = self.client.get(reverse('home:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_membership(self):
        response = self.client.get(reverse('home:membership'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'membership.html')

class TestHomepageHTML(TestCase):


    def test_for_some_html_elements(self):
        response = self.client.get(reverse('home:home'))
        self.assertInHTML("""<div class=\"issues sml-txt mt-4 \">
                            lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                            ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco 
                            laboris nisi ut aliquip ex ea commodo consequat.
                            <br /><br />
                            duis aute irure dolor in reprehenderit in voluptate 
                            velit esse cillum dolore eu fugiat nulla pariatur. excepteur sint occaecat cupidatat non proident, sunt
                            in culpa qui officia deserunt mollit anim id est laborum.
                            </div>""",
                          response.content.decode())

