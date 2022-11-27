from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import UserCreationForm, UserUpdateForm


class UserListView(ListView):
    model = User
    template_name = "users/list.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/create.html'
    next = "/"
    #
    # def get_success_url(self):
    #     messages.info(self.request, gettext_lazy('User created successfully'))
    #     return super().get_success_url(self)


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/edit.html'
    success_url = '/'

    def test_func(self):
        obj = self.get_object()
        if obj != self.request.user:
            messages.info(self.request, gettext_lazy('You cannot edit another user'))
            # redirect("/")
        return obj == self.request.user


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        username = request.user.username
        if self.get_form().is_valid():
            user = User.objects.get(pk=2)
            messages.info(request, gettext_lazy('User was successfully deleted'))
        return super().post(self, request, *args, **kwargs)

    # def tes

class UserLoginView(LoginView):
    # success_message = gettext_lazy('You are logged in')
    template_name = 'users/login.html'
    next_page = '/'

    def post(self, request, *args, **kwargs):
        if self.get_form().is_valid():
            messages.info(request, gettext_lazy('Login successfully'))
        return super().post(self, request, *args, **kwargs)


class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        messages.info(request, gettext_lazy('Logged out succesfully'))
        return redirect('/')
