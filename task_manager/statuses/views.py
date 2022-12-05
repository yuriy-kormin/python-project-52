from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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
        'statuses': _('statuses'),
        'ID': _('ID'),
        'name': _('name'),
        'created_at': _('created at'),
    }


class StatusCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('user_login')
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('create status'),
        'button_title': _('create'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Status created successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Status name already exists'))
        return super().form_invalid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('user_login')
    model = Status
    form_class = StatusForm
    template_name = "statuses/create.html"
    success_url = reverse_lazy('status_list')
    extra_context = {
        'header': _('update status'),
        'button_title': _('update'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Status updated successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Status name already exists'))
        return super().form_invalid(form)


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
        messages.info(self.request, _('status was deleted successfully'))
        return super().form_valid(form)
