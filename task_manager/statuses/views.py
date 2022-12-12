from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from django.utils.translation import gettext_lazy as _


class StatusListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user_login')
    model = Status
    template_name = "statuses/list.html"
    extra_context = {
        'statuses': _('Statuses'),
        'ID': _('ID'),
        'name': _('Name'),
        'created_at': _('Created at'),
    }


class StatusCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('user_login')
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Create status'),
        'button_title': _('Create'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Status created successfully'))
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('user_login')
    model = Status
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Update status'),
        'button_title': _('Update'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Status updated successfully'))
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('user_login')
    model = Status
    template_name = "statuses/delete.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('Remove status'),
        'button_title': _('Remove'),
        'message': _('Are you sure delete'),
    }
    raise_exception = False

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, _(
                'Status can\'t be deleted - on use now'))
        else:
            messages.info(self.request, _('Status was deleted successfully'))
        return redirect(self.get_success_url())
