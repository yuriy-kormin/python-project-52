from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
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


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('user_list')
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


# class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# class UserUpdateView(UpdateView):
#     model = User
#     form_class = UserForm
#     template_name = 'users/edit.html'
#     success_url = '/'
#     # raise_exception = True
#     login_url = '/login'
#
#     def test_func(self):
#         obj = self.get_object()
#         if obj != self.request.user:
#             messages.info(self.request, _('You cannot edit another user'))
#             # redirect("/")
#         return obj == self.request.user
#

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


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    next_page = reverse_lazy('root')
    extra_context = {
        'header': _('Enter'),
        'button_title': _('Enter'),
    }

    def form_valid(self, form):
        messages.info(self.request, _('Login successfully'))
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Login Error')
        return super().form_invalid(form)

    # def post(self, request, *args, **kwargs):
    #     if self.get_form().is_valid():
    #         messages.info(request, _('Login successfully'))
    #     elif self.get_form()
    #     return super().post(self, request, *args, **kwargs)


class UserLogoutView(LogoutView):

    def get(self, request):
        logout(request)
        messages.info(request, _('Logged out succesfully'))
        return redirect('/')
