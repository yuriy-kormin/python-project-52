from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _

class StatusListView(ListView):
    model = Status
    template_name = "statuses/list.html"
    extra_context = {
        'statuses': _('statuses'),
        'ID': _('ID'),
        'name': _('name'),
        'created_at': _('created at'),
    }


class StatusCreateView(CreateView):
    model = Status
    template_name = "statuses/create.html"


class StatusUpdateView(UpdateView):
    model = Status
    template_name = "statuses/update.html"

class StatusDeleteView(DeleteView):
    model = Status
    template_name = "statuses/delete.html"

