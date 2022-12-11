from task_manager.users.models import TaskUser as User
from django.urls import reverse_lazy as reverse
from django.test import TestCase
from ..models import Status, Task


class SelectStatus(TestCase):
    fixtures = ['db_task.json']
