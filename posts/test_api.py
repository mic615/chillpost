from django.test import TestCase
from django.contrib.auth.models import User
import json
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient


# initialize the APIClient app

# Create your tests here.
class  APITestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', email='test@gmail.com', password='top_secret')
        self.client = APIClient()
        self.valid_post_payload = {
            'body': 'test',
            'owner': self.user.id
        }
        self.invalid_post_payload = {
            'body': 'test'
        }

    def test_api_user_create_valid_post(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse('post-list'),
            data=json.dumps(self.valid_post_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_user_create_invalid_post(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse('post-list'),
            data=json.dumps(self.invalid_post_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
