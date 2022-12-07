from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, \
    DeleteView, DetailView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from .forms import TaskForm
from .models import Task
from task_manager.users.models import TaskUser as User


class TaskCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('user_login')
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'header': _('Add Task'),
        'button_title': _('Create'),
    }

    def form_valid(self, form):
        user = User.objects.get(pk=self.request.user.id)
        form.instance.author = user
        messages.success(self.request, _('Task created successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please fill form correctly'))
        return super().form_invalid(form)

    def get_login_url(self):
        messages.error(self.request, _('Please login to create tasks'))
        return super().get_login_url()


class TaskListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user_login')
    model = Task
    template_name = "tasks/list.html"
    extra_context = {
        'header': _('Tasks'),
        'ID': _('ID'),
        'task_header': _('name'),
        'status_header': _('Status'),
        'author_header': _('author'),
        'performer_header': _('performer'),
        'created_date_header': _('created at')
    }

    def get_login_url(self):
        messages.error(self.request, _('Please login to view tasks'))
        return super().get_login_url()


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task_list')
    login_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Edit task'),
        'button_title': _('Update'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Task update successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please fill form correctly'))
        return super().form_invalid(form)


class TaskDeleteView(UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'header': _('Remove task'),
        'button_title': _('Remove'),
        'message': _('Are you sure delete task '),
    }
    raise_exception = False

    def test_func(self):
        if self.request.user.is_authenticated:
            author_id = self.get_object().author_id
            author = User.objects.get(pk=author_id)
            user_id = self.request.user.id
            user = User.objects.get(pk=user_id)
            if user == author:
                return True
            messages.error(self.request,
                           _('You cannot delete another user tasks'))
        else:
            messages.error(self.request, _('Please login to delete tasks'))
        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('task_list'))
        return redirect(reverse_lazy('user_login'))

    def form_valid(self, form):
        messages.info(self.request, _('Task was successfully deleted'))
        return super().form_valid(form)


class TaskView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    login_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Task view'),
        'author': _('author'),
        'performer': _('performer'),
        'status': _('status'),
        'created': _('created'),
    }

    def get_login_url(self):
        messages.error(self.request, _('Please login to view tasks'))
        return super().get_login_url()
