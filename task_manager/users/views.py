from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from .models import TaskUser as User
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


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_login')

    extra_context = {
        'header': _('Register'),
        'button_title': _('Register '),
    }
    success_message = _('User created successfully')

    def form_invalid(self, form):
        for field in form.fields:
            if field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid '
            else:
                form[field].field.widget.attrs['class'] += ' is-valid '
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

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            user_instance = User.objects.get(pk=user.id)
            obj = self.get_object()
            object_instance = User.objects.get(pk=obj.id)
            if user_instance == object_instance:
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
        'button_title': _('Yes, remove'),
        'message': _('Are you sure delete'),
    }
    raise_exception = False

    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            user_instance = User.objects.get(pk=user.id)
            obj = self.get_object()
            object_instance = User.objects.get(pk=obj.id)
            if user_instance == object_instance:
                return True
            messages.error(self.request, _('You cannot delete another user'))
        else:
            messages.error(self.request, _('Please login to delete user'))
        return False

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        return redirect(reverse_lazy('user_login'))

    def form_valid(self, form):
        try:
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, _(
                'User can\'t be deleted - on use now'))
        else:
            messages.info(self.request, _('User was successfully deleted'))
        return redirect(self.get_success_url())
