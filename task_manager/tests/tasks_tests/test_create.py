from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.tasks.models import Status, Task


class Create(TestCase):
    fixtures = ['db_task.json']

    def test_create_open_without_login(self):
        response = self.client.get(reverse('task_add'))
        self.assertEqual(response.status_code, 302)

    def test_create_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        status = Status.objects.all().first()
        response = self.client.get(reverse('task_add'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 1)
        response = self.client.post(
            reverse('task_add'),
            {'name': 'test task',
             'author': user.id,
             'status': status.id
             }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.all().count(), 2)
