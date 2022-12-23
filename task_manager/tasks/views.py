from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, \
    DeleteView, DetailView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from .filters import MarkFilter
from .forms import TaskForm
from .mixins import DeleteTaskMixin, SetAuthorMixin
from .models import Task
from django_filters.views import FilterView
from task_manager.mixins import LoginRequiredCustomMixin


class TaskCreateView(LoginRequiredCustomMixin, SuccessMessageMixin,
                     SetAuthorMixin, CreateView):
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'header': _('Add Task'),
        'button_title': _('Create'),
    }
    success_message = _('Task created successfully')
    permission_denied_message = _('Please login')


class TaskListView(LoginRequiredCustomMixin, FilterView, ListView):
    filterset_class = MarkFilter
    model = Task
    template_name = "tasks/list.html"
    extra_context = {
        'select': _('Select'),
        'header': _('Tasks'),
        'ID': _('ID'),
        'task_header': _('Name'),
        'status_header': _('Status'),
        'author_header': _('Author'),
        'performer_header': _('Performer'),
        'created_date_header': _('Created at')
    }
    permission_denied_message = _('Please login')


class TaskUpdateView(LoginRequiredCustomMixin, SuccessMessageMixin,
                     UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'header': _('Edit task'),
        'button_title': _('Update'),
    }
    success_message = _('Task updated successfully')
    permission_denied_message = _('Please login')


class TaskDeleteView(LoginRequiredCustomMixin, DeleteTaskMixin,
                     SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('task_list')
    extra_context = {
        'header': _('Remove task'),
        'button_title': _('Remove '),
        'message': _('Are you sure delete task '),
    }
    permission_denied_message = _('Please login')
    delete_error_message = _('You cannot delete another user tasks')
    success_message = _('Task was successfully deleted')


class TaskView(LoginRequiredCustomMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    extra_context = {
        'header': _('Task view'),
        'author': _('author'),
        'executor': _('executor'),
        'status': _('status'),
        'created': _('created'),
        'labels': _('labels'),
    }
    permission_denied_message = _('Please login')
