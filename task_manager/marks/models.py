from django.db import models


class Mark(models.Model):
    name = models.CharField(max_length=200, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
