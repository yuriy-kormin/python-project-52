from django.urls import reverse_lazy as reverse
from django.test import TestCase
from django.contrib.auth.models import User


class Delete(TestCase):

    def setUp(self):
        User.objects.create_user(username='john', password='smith')

    def test_delete(self):
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': 1}
            )
        )
        self.assertRedirects(response, reverse('user_list'))
        users = User.objects.all()
        self.assertEqual(len(users), 0)

    def test_delete_only_himself(self):
        user1 = User.objects.get(pk=1)
        User.objects.create_user(username='john2', password='smith')
        self.client.login(username='john2', password='smith')
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': 1}
            )
        )
        self.assertRedirects(response, reverse('user_list'))
        users = User.objects.all()
        self.assertIn(user1, users)
