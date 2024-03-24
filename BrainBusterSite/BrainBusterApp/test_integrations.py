from django.test import TestCase, Client
from django.urls import reverse
from BrainBusterApp.models import Score
from django.contrib.auth.models import User

class IntegrationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("rankings")

    def test_user_rankings(self):
        # create user via register site
        register_response = self.client.post('/accounts/register/', {'username': ['john'], 'email': ['lennon@thebeatles.com'], 'password1': ['sicheres_p12'], 'password2': ['sicheres_p12']})

        # test register success
        self.assertEqual(register_response.status_code, 302)

        # Send a GET request to rankings
        response = self.client.get(self.url)

        # Assert the response status code and content
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 0)
