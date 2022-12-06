from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser as User
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'performer',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('name'),
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('description'),
                }
            ),
            'status': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choices': Status,
                }
            ),
            'performer': forms.Select(
                attrs={
                    'class': 'form-control',
                    'choices': User,
                }
            ),
        }
        labels = {
            'name': _('name'),
            'description': _('description'),
            'status': _('status'),
            'performer': _('performer'),
        }
