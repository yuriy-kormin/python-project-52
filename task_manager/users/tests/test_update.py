import json
from django.urls import reverse_lazy as reverse
from django.test import TestCase
import os
from django.contrib.auth.models import User

FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '../fixtures'
)

FIXTURE_FILE = os.path.join(FIXTURE_DIR, 'user.json')
TEST_USER = json.load(open(FIXTURE_FILE))


class Modify(TestCase):
    fixtures = ['db.json']
    username = TEST_USER.get('username')
    psw = TEST_USER.get('password1')

    def setUp(self):
        User.objects.create_user(
            username=self.username,
            password=self.psw,
        )

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
        self.client.login(username=self.username, password=self.psw)
        updated_user = TEST_USER.copy()
        updated_user['first_name'] = 'Captain'
        updated_user['last_name'] = 'Cook'
        updated_user['username'] = 'capcook'
        updated_user['password1'] = 'capcookpass'
        updated_user['password2'] = updated_user['password1']

        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 2}
            ),
            updated_user
        )
        self.assertRedirects(response, reverse('user_list'))
        user = User.objects.get(pk=2)
        self.assertEqual(user.first_name, updated_user.get('first_name'))
        self.assertEqual(user.last_name, updated_user.get('last_name'))
        self.assertEqual(user.username, updated_user.get('username'))

    def test_modify_only_himself(self):
        User.objects.create_user(username='john', password='smith')
        self.client.login(username='john', password='smith')
        response = self.client.post(
            reverse(
                'user_update',
                kwargs={'pk': 1}
            ),
            TEST_USER
        )
        self.assertRedirects(response, reverse('user_list'))
        user = User.objects.get(pk=1)
        self.assertNotEqual(user.username, TEST_USER['username'])
