from django.db import models


class Status(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.name
