from django import forms
from django.utils.translation import gettext_lazy as _
from .models import TaskUser as User
from django.core.validators import MinLengthValidator


class UserForm(forms.ModelForm):
    password_min_len = 3

    first_name = forms.CharField(
        label=_('First name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('First name'),
            }
        )
    )

    last_name = forms.CharField(
        label=_('Last name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Last name'),
            }
        )
    )

    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Username'),
                'title': _('Not an option')
            }
        )
    )

    password1 = forms.CharField(
        validators=[
            MinLengthValidator(password_min_len,
                               _("Password is too short")),
        ],
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password'),
                'title': _('Password must contains at least 3 chars')
            }
        )
    )
    password2 = forms.CharField(
        label=_('Password confirmation'),
        validators=[
            MinLengthValidator(password_min_len,
                               _("Password is too short")),
        ],
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Password confirmation'),
                'title': _('Please, type your password again'),
            }
        )
    )

    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _("Passwords don't match"), code='invalid')
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(
                username=username).exists():
            raise forms.ValidationError(
                _('Username already exists'),
                code='invalid')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
