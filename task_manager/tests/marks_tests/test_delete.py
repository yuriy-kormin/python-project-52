from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from task_manager.marks.models import Mark


class DeleteMark(TestCase):
    fixtures = ['db_mark.json']

    def test_delete_open_without_login(self):
        response = self.client.get(reverse('mark_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        user = User.objects.all().first()
        self.client.force_login(user=user)
        response = self.client.get(reverse('mark_delete', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse('mark_delete', kwargs={'pk': 1})
        )
        statuses = Mark.objects.all()
        self.assertEqual(len(statuses), 0)
