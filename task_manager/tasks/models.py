from django.db import models
from task_manager.users.models import TaskUser as User
from task_manager.statuses.models import Status


class Task(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=400)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='author')
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    performer = models.ForeignKey(User, on_delete=models.PROTECT,
                                  related_name='performer')
