from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase


class List(TestCase):
    fixtures = ['db_status.json']

    def test_open_create_without_login(self):
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 302)

    def test_list_with_login(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_list'))
        self.assertEqual(response.status_code, 200)
