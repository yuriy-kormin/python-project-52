from django.db import models
from task_manager.users.models import TaskUser as User
from task_manager.statuses.models import Status


class Task(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=400)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='author',
        blank=False, null=False)
    status = models.ForeignKey(to=Status, on_delete=models.PROTECT,
                               blank=False, null=False)
    performer = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='performer',
        blank=True, null=True)
