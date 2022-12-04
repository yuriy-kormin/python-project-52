from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.statuses.models import Status


class StatusListView(ListView):
    model = Status
    template_name = "statuses/list.html"


class StatusCreateView(CreateView):
    model = Status
    template_name = "statuses/create.html"


class StatusUpdateView(UpdateView):
    model = Status
    template_name = "statuses/update.html"

class StatusDeleteView(DeleteView):
    model = Status
    template_name = "statuses/delete.html"

