from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages

from .models import Ramal


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['topos'] = Ramal.objects.order_by('?').all()
        return context

