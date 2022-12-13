from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Mark


class MarkForm(forms.ModelForm):

    class Meta:
        model = Mark
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name')
                }
            ),
        }
        labels = {
            'name': _('Name'),
        }
