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

# from django.test import Client, TestCase
#
#
# class WebTest(TestCase):
#
#     def test_root_get(self):
#         c = Client()
#         response = c.get('/login/')  # , {'username': 'john', 'password': 'smith'})
#         self.assertTrue(response.status_code == 200)

# from django.test import TestCase
# # from .models import
# from django.utils import timezone
# # from django.core.urlresolvers import reverse
# from .forms import UserForm
# from django.contrib.auth.models import User
#
# # models test
# class UserTest(TestCase):
#
#     def create_user(self, title="only a test", body="yes, this is only a test"):
#         return User.objects.create(
#             first_name=title,
#             last_name=title,
#             username=title,
#             password='123',
#             # created_at=timezone.now(),
#         )
#
#     def test__creation(self):
#         w = self.create_user()
#         self.assertTrue(isinstance(w, User))
#         self.assertTrue(w.first_name == 'only a test')
#         # self.assertEqual(w.__unicode__(), w.title)
