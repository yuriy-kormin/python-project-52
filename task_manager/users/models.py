from django.contrib.auth.models import User


class TaskUser(User):

    def __str__(self):
        return " ".join((str(self.first_name), str(self.last_name)))
