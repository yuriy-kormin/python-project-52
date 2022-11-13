from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .forms import UserForm


class UserListView(ListView):
    model = User
    template_name = "users/list.html"


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = '/'


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit.html'
    success_url = '/'


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/'


class UserLoginView(View):
    def get(self, request):
        pass


class UserLogoutView(View):
    def get(self, request):
        pass
