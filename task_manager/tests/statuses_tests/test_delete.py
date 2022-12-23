from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.statuses.models import Status


class Deletestatus(TestCase):
    fixtures = ['db_status.json']

    def test_delete_open_without_login(self):
        response = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('status_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('status_delete', kwargs={'pk': 1})
        )
        statuses = Status.objects.all()
        self.assertEqual(len(statuses), 0)
