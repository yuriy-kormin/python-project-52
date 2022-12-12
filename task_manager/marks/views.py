from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import MarkForm
from .models import Mark
from django.utils.translation import gettext_lazy as _


class MarkCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('user_login')
    form_class = MarkForm
    template_name = "marks/create.html"
    success_url = reverse_lazy('mark_list')
    extra_context = {
        'header': _('create mark'),
        'button_title': _('create'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Mark created successfully'))
        return super().form_valid(form)


class MarkListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('user_login')
    model = Mark
    template_name = "marks/list.html"
    extra_context = {
        'marks': _('marks'),
        'ID': _('ID'),
        'name': _('name'),
        'created_at': _('created at'),
    }


class MarkUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('user_login')
    model = Mark
    form_class = MarkForm
    template_name = "marks/create.html"
    success_url = reverse_lazy('mark_list')
    extra_context = {
        'header': _('update mark'),
        'button_title': _('update'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('Mark updated successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Mark name already exists'))
        return super().form_invalid(form)


class MarkDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('user_login')
    model = Mark
    template_name = "marks/delete.html"
    success_url = reverse_lazy('mark_list')
    extra_context = {
        'header': _('Remove mark'),
        'button_title': _('Remove'),
        'message': _('Are you sure delete'),
    }
    raise_exception = False

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, _(
                'Mark can\'t be deleted - on use now'))
        else:
            messages.info(self.request, _('Mark was deleted successfully'))
        return redirect(self.get_success_url())
