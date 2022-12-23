from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.tasks.models import Task


class DeleteTask(TransactionTestCase):
    fixtures = ['db_task.json']

    def test_delete_task_open_without_login(self):
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('task_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('task_delete', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.all().count(), 0)
