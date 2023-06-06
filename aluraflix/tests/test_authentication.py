from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('programas-list')
        self.user = User.objects.create_user('c3po', password='12345')

    def test_user(self):
        user = authenticate(username='c3po', password='12345')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_unauthorized_request(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_incorrect_username_authentication(self):
        user = authenticate(username='c3pp', password='12345')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_incorrect_password_authentication(self):
        user = authenticate(username='c3po', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_user_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)