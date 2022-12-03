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
# class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_list')
    login_url = reverse_lazy('user_login')
    # permission_denied_message = _('You cannot edit another user')
    # raise_exception = True
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
        obj = self.get_object()
        if obj != self.request.user:
            messages.error(self.request, _('You cannot edit another user'))
        return obj == self.request.user

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(self.success_url)
        messages.error(self.request, _('Please login to modify user'))
        return redirect(self.login_url)

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         raise ConnectionError
    #         if request.get_object != self.request.user:
    #             messages.error(self.request, _('You cannot edit another user'))
    #             return redirect(reverse_lazy('user_list'))
    #     return super().dispatch(request,*args,**kwargs)
    # def handle_no_permission(self):
    #     if self.request.user.is_authenticated:
    #         if self.request.object != self.request.user:
    #             messages.error(self.request, _('You cannot edit another user'))
    #             return redirect(reverse_lazy('user_list'))
    #     else:
    #         return redirect(reverse_lazy('user_login'))


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/'
    extra_context = {
        'header': _('Remove user'),
        'button_title': _('Remove'),
        'message': _('Are you sure delete'),
    }

    #
    # def post(self, request, *args, **kwargs):
    #     username = request.user.username
    #     if self.get_form().is_valid():
    #         user = User.objects.get(pk=2)
    #         messages.info(request, gettext_lazy('User was successfully deleted'))
    #     return super().post(self, request, *args, **kwargs)

    # def tes
