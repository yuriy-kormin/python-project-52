from django.shortcuts import render
from task_manager.users.models import User
from django.utils.translation import gettext


def user_list(request):
    users = User.objects.all()
    # users = [{'first_name':'vasya'},
    #          {'first_name':'fedya'}]

    return render(request, 'users/list.html', {
        'users': users,
    })
