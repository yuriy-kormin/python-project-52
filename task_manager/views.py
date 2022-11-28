# from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {
        'header': _('Task manager'),
    }


