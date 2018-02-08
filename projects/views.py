"""
ThunderSite - ThundeRatz

Projects Pages Views
Daniel Nery Silva de Oliveira

01/2018
"""

from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Project, SuperCategory, Category

# Create your views here.
class ProjectListView(ListView):
    template_name = 'projects/index.html'
    model = Project
    context_object_name = 'project_list'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
