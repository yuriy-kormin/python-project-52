from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import MarkForm
from .models import Mark
from django.utils.translation import gettext_lazy as _
from ..mixins import LoginRequiredCustomMixin, DeleteProtectErrorMixin


class MarkCreateView(LoginRequiredCustomMixin, SuccessMessageMixin,
                     CreateView):
    form_class = MarkForm
    template_name = "marks/create.html"
    success_url = reverse_lazy('mark_list')
    extra_context = {
        'header': _('Create mark'),
        'button_title': _('Create'),
    }
    success_message = _('Mark created successfully')
    permission_denied_message = _('Please login')


class MarkListView(LoginRequiredCustomMixin, ListView):
    model = Mark
    template_name = "marks/list.html"
    extra_context = {
        'marks': _('Marks'),
        'ID': _('ID'),
        'name': _('Name'),
        'created_at': _('Created at'),
    }
    permission_denied_message = _('Please login')


class MarkUpdateView(LoginRequiredCustomMixin, SuccessMessageMixin,
                     UpdateView):
    model = Mark
    form_class = MarkForm
    template_name = "marks/create.html"
    success_url = reverse_lazy('mark_list')
    extra_context = {
        'header': _('Update mark'),
        'button_title': _('Update'),
    }
    success_message = _('Mark updated successfully')
    permission_denied_message = _('Please login')


class MarkDeleteView(LoginRequiredCustomMixin, DeleteProtectErrorMixin,
                     DeleteView):
    model = Mark
    template_name = "marks/delete.html"
    success_url = reverse_lazy('mark_list')
    extra_context = {
        'header': _('Remove mark'),
        'button_title': _('Yes, remove'),
        'message': _('Are you sure delete'),
    }
    raise_exception = False
    permission_denied_message = _('Please login')
    protected_error_message = _('Mark can\'t be deleted - on use now')
    success_message = _('Mark was deleted successfully')
