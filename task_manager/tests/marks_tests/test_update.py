from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.marks.models import Mark


class UpdateStatus(TestCase):
    fixtures = ['db_mark.json']

    def test_update_open_without_login(self):
        response = self.client.get(reverse('mark_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_update_mark(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_update', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('mark_update', kwargs={'pk': 1}),
            {'name': 'test'}
        )
        mark = Mark.objects.get(pk=1)
        self.assertEqual(mark.name, 'test')
