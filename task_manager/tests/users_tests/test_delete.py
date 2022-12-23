from django.urls import reverse_lazy as reverse
from django.test import TransactionTestCase
from task_manager.users.models import TaskUser as User
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class Delete(TransactionTestCase):
    fixtures = ['db.json']

    def test_delete_without_login(self):
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': 1}
            )
        )
        self.assertRedirects(response, reverse('user_login'))
        users = User.objects.all().count()
        self.assertEqual(users, 1)

    def test_delete_only_himself(self):
        user1 = User.objects.all().first()
        user2 = User.objects.create_user(username='john', password='smith')
        self.client.login(username='john', password='smith')
        response = self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user1.id}
            )
        )
        self.assertRedirects(response, reverse('user_list'))
        self.assertIn(user1, User.objects.all())
        self.assertEqual(User.objects.all().count(), 2)
        self.client.post(
            reverse(
                'user_delete',
                kwargs={'pk': user2.id}
            )
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertNotIn(user2, User.objects.all())

    def test_delete_with_tasks(self):
        status = Status(name='open status')
        user = User.objects.all()[0]
        status.save()
        task = Task(
            name="Simp Task",
            status=status,
            author=user,
        )
        task.save()
