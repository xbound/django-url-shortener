from django.test import TestCase, Client
from django.shortcuts import reverse

class UrlShortenerTestCase(TestCase):

    def test_shorten_url(self):
        response = self.client.post(reverse('urlshortener:shorten'), {'url': 'https://docs.djangoproject.com/en/3.2/topics/templates/#configuration'})
        self.assertTrue(response.status_code == 200)
        self.assertIn('shortened_url', response.json())
    
    def test_go_to_url(self):
        response = self.client.post(reverse('urlshortener:shorten'), {'url': 'https://docs.djangoproject.com/en/3.2/topics/templates/#configuration'})
        self.assertTrue(response.status_code == 200)
        hashed_url = response.json()['shortened_url']
        response = self.client.get(hashed_url)
        self.assertTrue(response.status_code == 302)


