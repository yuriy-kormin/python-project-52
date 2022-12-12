import django_filters
from django import forms
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import TaskUser as User
from django.utils.translation import gettext_lazy as _
from task_manager.marks.models import Mark


class MarkFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        label=_('Status'),
        queryset=lambda req: Status.objects.all(),
    )
    executor = django_filters.ModelChoiceFilter(
        label=_('Performer'),
        queryset=lambda req: User.objects.all(),
        field_name='performer',
    )
    label = django_filters.ModelChoiceFilter(
        label=_('Mark'),
        queryset=lambda req: Mark.objects.all(),
        field_name='mark'
    )
    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        label=_('Only self tasks'),
        method='get_self_tasks'
    )

    def get_self_tasks(self, queryset, field_name, value):
        result = queryset.filter(author_id=self.request.user.id)
        return result if value else queryset

    class Meta:
        model = Task
        fields = []
