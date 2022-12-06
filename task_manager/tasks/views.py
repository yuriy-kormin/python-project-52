from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect

# Create your views here.
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
        'task_name': _('name'),
        'status_name': _('Status'),
        'author_name': _('author'),
    }

    def get_login_url(self):
        messages.error(self.request, _('Please login to view tasks'))
        return super().get_login_url()


class TaskUpdateView(LoginRequiredMixin,UpdateView):
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
    pass


class TaskView(LoginRequiredMixin, DetailView):
    pass