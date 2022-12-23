import json
from django.urls import reverse_lazy as reverse
from django.test import TestCase
import os
from task_manager.users.models import TaskUser as User
FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)


class CreateTest(TestCase):

    def test_open_create_page(self):
        response = self.client.get(reverse('user_add'))
        self.assertEqual(response.status_code, 200)

    def test_create_redirect_user(self):
        fixture_file = os.path.join(FIXTURE_DIR, 'user.json')
        testuser = json.load(open(fixture_file))
        response = self.client.post(
            reverse('user_add'),
            testuser
        )
        self.assertRedirects(response, reverse('user_login'))
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, testuser.get('username'))
