from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = (
                  'name',
                  # 'date_joined',
                  )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('name')
                }
            ),
        }
        labels = {
            'name': _('name'),
        }

