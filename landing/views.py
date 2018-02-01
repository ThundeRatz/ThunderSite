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
        context['menu2'] = 'Equipe'
        context['menu3'] = 'Projetos'
        context['menu4'] = 'História'
        context['menu5'] = 'Patrocinadores'
        context['menu6'] = 'Contato'

        context['list_gold'] = [x for x in range(1, 8)]     # TODO put actual sponsor here
        context['list_silver'] = [x for x in range(1, 11)]

        context['events'] = Event.objects.all()

        return context
