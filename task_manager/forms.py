from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import TaskUser as User


class LoginForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     kwargs.setdefault('label_suffix', '')
    #     return super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ('username',
                  'password',
                  )
        # widgets ={
        #     'username':forms.TextInput(
        #         attrs={
        #             "label_suffix": "",
        #         }
        #     )

        # }