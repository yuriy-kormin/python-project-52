from django import forms
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser as User
from .models import Task
from task_manager.marks.models import Mark


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'performer',
            'mark',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': _('Name'),
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
            'mark': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'choices': Mark,
                }
            ),
        }
        labels = {
            'name': _('Name'),
            'description': _('description'),
            'status': _('status'),
            'performer': _('performer'),
            'mark': _('Marks')
        }
