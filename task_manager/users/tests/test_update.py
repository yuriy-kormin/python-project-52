import json
from django.urls import reverse_lazy as reverse
from django.test import TestCase
import os
from django.contrib.auth.models import User

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'fixtures'
)

FIXTURE_FILE = os.path.join(FIXTURE_DIR, 'user.json')
TEST_USER = json.load(open(FIXTURE_FILE))


class Modify(TestCase):
    def setUp(self):
        User.objects.create_user(username='john', password='smith')

    def test_modify_only_logged(self):
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 1}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('user_login'))

    def test_modify_redirect_after_logging(self):
        self.client.login(username='john', password='smith')
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 1}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('user_list'))
        user1 = User.objects.get(pk=1)
        self.assertEqual(user1.username, TEST_USER.get('username'))

    def test_modify_only_himself(self):
        User.objects.create_user(username='john2', password='smith')
        self.client.login(username='john2', password='smith')
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 1}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('user_list'))
        user2 = User.objects.get(pk=2)
        self.assertEqual(user2.username, 'john2')
