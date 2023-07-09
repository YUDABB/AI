from django.test import TestCase,Client
from bs4 import BeautifulSoup
#from .models import intro

# Create your tests here.
class TestView(TestCase):

    def setUp(self):
        self.client = Client()

    def test_intro_profile(self):
        response = self.client.get('/intro')