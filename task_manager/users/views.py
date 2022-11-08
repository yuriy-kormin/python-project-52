from django.shortcuts import render
from django.views import View
from .models import User
from .forms import UserForm


class UserAddView(View):
    def get(self, request):
        pass
    # if request.method == 'POST':
    #     form = UserForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = UserForm()
    # return render(request, 'users/list.html', context={'form': form})


class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users/list.html', context={
            'users': users,
        })
