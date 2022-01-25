"""
ThunderSite - ThundeRatz

Landing Page view
Daniel Nery Silva de Oliveira

01/2018
"""

from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from .models import Event, Sponsor, About, Recruitment, ProgressBar
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
        context["thunder_donations"] = ProgressBar.objects.get(name="thunder_donations")

        return context


class RecruitmentView(TemplateView):
    template_name = "landing/recruitment.html"

    def get_context_data(self, **kwargs):
        context = super(RecruitmentView, self).get_context_data(**kwargs)
        context["recruitment"] = Recruitment.objects.all()[0]

        return context

