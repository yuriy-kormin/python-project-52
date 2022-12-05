from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UserForm


class UserListView(ListView):
    model = User
    template_name = "users/list.html"
    extra_context = {
        'header': _('Users'),
        'ID': _('ID'),
        'username': _('username'),
        'full_name': _('full name'),
        'created_at': _('create at'),
    }


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Register'),
        'button_title': _('Register'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('User created successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please fill form correctly'))
        return super().form_invalid(form)


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_list')
    login_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Edit user'),
        'button_title': _('Update'),
    }

    def form_valid(self, form):
        messages.success(self.request, _('User update successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, _('Please fill form correctly'))
        return super().form_invalid(form)

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user == self.get_object():
                return True
            messages.error(self.request, _('You cannot edit another user'))
        else:
            messages.error(self.request, _('Please login to modify user'))
        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return redirect(self.login_url)


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')
    extra_context = {
        'header': _('Remove user'),
        'button_title': _('Remove'),
        'message': _('Are you sure delete'),
    }
    raise_exception = False

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user == self.get_object():
                return True
            messages.error(self.request, _('You cannot delete another user'))
        else:
            messages.error(self.request, _('Please login to delete user'))
        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(reverse_lazy('user_list'))
        return redirect(reverse_lazy('user_login'))

    def form_valid(self, form):
        messages.info(self.request, _('User was successfully deleted'))
        return super().form_valid(form)
