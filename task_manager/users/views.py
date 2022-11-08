from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import User
from .forms import UserForm


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/list.html', context={
            'users': users,
        })


class UserCreateView(View):
    def get(self, request):
        if request.method == 'POST':
            form = UserForm(request.POST)

            if form.is_valid():
                form.save()
        else:
            form = UserForm()
        return render(request, 'users/create.html', context={'form': form})


class UserUpdateView(View):
    def get(self, request):
        pass


class UserDeleteView(View):
    def get(self, request):
        pass


class UserLoginView(View):
    def get(self, request):
        pass


class UserLogoutView(View):
    def get(self, request):
        pass
