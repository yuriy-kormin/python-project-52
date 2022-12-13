from django.db import models
from task_manager.marks.models import Mark
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
    label = models.ManyToManyField(to=Mark, through='Bond',
                                   blank=True, null=True)
    executor = models.ForeignKey(
        to=User, on_delete=models.PROTECT,
        blank=True, null=True)


class Bond(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)
