from django.db import models


class Status(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField()
