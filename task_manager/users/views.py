from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView,UpdateView

from .models import User
from .forms import UserForm


class UserListView(ListView):
    model = User
    template_name = "users/list.html"


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = '/'
    # def get(self, request):
    #     if request.method == 'POST':
    #         form = UserForm(request.POST)
    #         print (request.POST)
    #     return render(request, 'users/create.html', context={'form': form})
    #
    # def form_valid(self, form):
    #
    #     return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    # for
    template_name = 'users/create.html'


class UserDeleteView(DeleteView):
    model = User


class UserLoginView(View):
    def get(self, request):
        pass


class UserLogoutView(View):
    def get(self, request):
        pass
