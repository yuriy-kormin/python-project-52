from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from task_manager.users.models import TaskUser as User


class DeleteTaskMixin(UserPassesTestMixin):
    delete_error_message = ''
    success_url = ''

    def test_func(self):
        author = User.objects.get(pk=self.get_object().author_id)
        user = User.objects.get(pk=self.request.user.id)
        if user == author:
            return True
        return False

    def handle_no_permission(self):
        messages.error(self.request, self.delete_error_message)
        return redirect(self.success_url)


class SetAuthorMixin:
    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.id)
        form.instance.author = user
        return super().form_valid(form)
