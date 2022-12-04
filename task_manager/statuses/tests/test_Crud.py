from django.urls import reverse_lazy as reverse
from django.test import TestCase
from ..models import Status


class Create(TestCase):

    def test_open_create_without_login(self):
        response = self.client.get(reverse('status_add'))
        self.assertEqual(response.status_code, 302)