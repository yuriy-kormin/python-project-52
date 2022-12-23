from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.statuses.models import Status


class Create(TestCase):
    fixtures = ['db_status.json']

    def test_create_open_without_login(self):
        response = self.client.get(reverse('status_add'))
        self.assertEqual(response.status_code, 302)

    def test_create_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        statuses = Status.objects.all()
        response = self.client.get(reverse('status_add'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(statuses), 1)
        response = self.client.post(
            reverse('status_add'),
            {'name': 'test'}
        )
        statuses2 = Status.objects.all()
        self.assertEqual(len(statuses2), 2)
        status_added = statuses2[1]
        self.assertEqual(status_added.name, 'test')
