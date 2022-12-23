from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.statuses.models import Status


class DeleteStutusWithTask(TransactionTestCase):
    fixtures = ['db_task_two_users.json']

    def test_delete_with_task(self):
        status = Status.objects.all().first()
        user = User.objects.all().first()
        self.assertEqual(Status.objects.all().count(), 1)
        self.client.force_login(user=user)
        self.client.get(reverse('status_delete',
                                kwargs={'pk': status.id}))
        self.assertEqual(Status.objects.all().count(), 1)
