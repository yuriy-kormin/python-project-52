from django.contrib.auth.mixins import AccessMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import UserCreationForm, LoginForm, UserUpdateForm


class UserListView(ListView):

    model = User
    template_name = "users/list.html"


class UserCreateView(SuccessMessageMixin,AccessMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'users/create.html'
    success_url = '/'
    success_message = 'User created succesfully'
    permission_denied_message = " error"

    # def get(self, request,*args,**kwargs):


class UserUpdateView(SuccessMessageMixin,AccessMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/edit.html'
    success_message = 'Data was updated'
    permission_denied_message = 'second error'
    success_url = '/'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/'


class UserLoginView(SuccessMessageMixin, LoginView):
    # authentication_form = LoginForm
    success_message = 'You are logged in'
    template_name = 'users/login.html'
    next_page = '/'
    # next_page = '/'
    #
    # def get(self, request):
    #     pass


class UserLogoutView(View):
    def get(self, request):
        pass
