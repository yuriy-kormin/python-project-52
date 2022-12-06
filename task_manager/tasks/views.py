from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, \
    DeleteView, DetailView
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from task_manager.tasks.models import Task


class TaskCreateView(CreateView):
    pass


class TaskListView(ListView):
    model = Task
    template_name = "tasks/list.html"
    extra_context = {
        'header': _('Tasks'),
        'ID': _('ID'),
        'task_name': _('name'),
        'status_name': _('Status'),
        'author_name': _('author'),
    }


class TaskUpdateView(UpdateView):
    pass


class TaskDeleteView(DeleteView):
    pass


class TaskView(DetailView):
    pass