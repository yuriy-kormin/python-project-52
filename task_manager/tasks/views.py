from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, \
    DeleteView, DetailView
from django.views.generic import ListView


class TaskCreateView(CreateView):
    pass


class TaskListView(ListView):
    pass


class TaskUpdateView(UpdateView):
    pass


class TaskDeleteView(DeleteView):
    pass


class TaskView(DetailView):
    pass