from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.marks.models import Mark


class Create(TestCase):
    fixtures = ['db_mark.json']

    def test_create_open_without_login(self):
        response = self.client.get(reverse('mark_add'))
        self.assertEqual(response.status_code, 302)

    def test_create_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_add'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Mark.objects.all().count(), 1)
        response = self.client.post(
            reverse('mark_add'),
            {'name': 'test'}
        )
        self.assertEqual(Mark.objects.all().count(), 2)
