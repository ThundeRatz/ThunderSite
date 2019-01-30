"""
ThunderSite - ThundeRatz

Landing Page view
Daniel Nery Silva de Oliveira

01/2018
"""

from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Event, Sponsor, About
from news.models import News


class IndexView(TemplateView):
    template_name = "landing/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["sponsors"] = Sponsor.objects.all()
        context["events"] = Event.objects.all()
        context["news"] = News.objects.all()[:3]
        context["the_team"] = About.objects.get(type="A")
        context["workshop"] = About.objects.get(type="B")

        return context
