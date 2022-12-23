from django.contrib.messages.views import SuccessMessageMixin
from .mixins import UserTestCustomMixin
from .models import TaskUser as User
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UserForm
from task_manager.mixins import LoginRequiredCustomMixin,\
    DeleteProtectErrorMixin


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


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Register'),
        'button_title': _('Register '),
    }
    success_message = _('User created successfully')


class UserUpdateView(LoginRequiredCustomMixin, UserTestCustomMixin,
                     SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_list')
    # login_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Edit user'),
        'button_title': _('Update'),
    }
    permission_denied_message = _('Please login to modify user')
    modify_error_message = _('You cannot edit another user')
    success_message = _('User update successfully')


class UserDeleteView(LoginRequiredCustomMixin, UserTestCustomMixin,
                     DeleteProtectErrorMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('user_list')
    # login_url = reverse_lazy('user_login')
    extra_context = {
        'header': _('Remove user'),
        'button_title': _('Yes, remove'),
        'message': _('Are you sure delete'),
    }
    permission_denied_message = _('Please login to delete user')
    modify_error_message = _('You cannot delete another user')
    success_message = _('User was successfully deleted')
    protected_error_message = _('User can\'t be deleted - on use now')
