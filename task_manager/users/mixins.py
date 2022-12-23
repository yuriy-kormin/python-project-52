from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from .models import TaskUser as User


class UserTestCustomMixin(UserPassesTestMixin):
    modify_error_message = ''
    success_url = ''

    def test_func(self):
        user_instance = User.objects.get(pk=self.request.user.id)
        obj = self.get_object()
        object_instance = User.objects.get(pk=obj.id)
        if user_instance == object_instance:
            return True
        return False

    def handle_no_permission(self):
        messages.error(self.request, self.modify_error_message)
        return redirect(self.success_url)
