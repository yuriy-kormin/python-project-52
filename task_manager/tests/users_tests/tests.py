from django.urls import reverse_lazy as reverse
from django.test import TestCase


class SimpleTest(TestCase):

    def test_page_contains_links(self):
        list_links = [
            'user_list',
            'user_add',
            'user_login',
        ]
        response = self.client.get('/')
        for path in map(reverse, list_links):
            self.assertContains(response, path)

    def test_userlist_access_without_login(self):
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
