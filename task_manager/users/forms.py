from django import forms
# from .models import User
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name',
#                   'last_name',
#                   'username',
#                   'password'
#                   )
#         widgets = {
#            # 'username': forms.TextInput(attrs={'placeholder': 'username'}),
#             'password': forms.TextInput(),
#         # .widget.attrs['placeholder'] = 'username'
#         }
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user
#
from django.http import HttpResponse


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  )
        # localized_fields = ('__all__')
        widgets ={
            'first_name': forms.TextInput(attrs={'placeholder': _('first name')}),
            'last_name': forms.TextInput(attrs={'placeholder': _('last name')}),
            'username': forms.TextInput(attrs={'placeholder': _('username')}),
            # 'password1': forms.CharField(attrs={'placeholder': _('password')})
            # 'password1':forms.CharField(attrs)
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  # 'password'
                  )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            # messages.info(request, 'User not exist')
            raise ValidationError(_("Passwords don't match"))
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')