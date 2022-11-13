from django import forms
# from .models import User
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'password'
                  )
        widgets = {
           # 'username': forms.TextInput(attrs={'placeholder': 'username'}),
            'password': forms.PasswordInput(),
        # .widget.attrs['placeholder'] = 'username'
        }