"""
ThunderSite - ThundeRatz

Landing Page view
Daniel Nery Silva de Oliveira

01/2018
"""

from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Event, Sponsor

class IndexView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu1'] = 'Início'
        context['menu2'] = 'Projetos'
        context['menu3'] = 'História'
        context['menu4'] = 'Patrocinadores'
        context['menu5'] = 'Contato'

        context['sponsors'] = Sponsor.objects.all()

        context['events'] = Event.objects.all()

        return context
