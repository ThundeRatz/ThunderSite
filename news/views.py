"""
ThunderSite - ThundeRatz

News Pages Views
Daniel Nery Silva de Oliveira

01/2018
"""

from django.views.generic import View, TemplateView, ListView, DetailView
from .models import News

# TODO put the ListView, with the models
class NewsListView(TemplateView):
    template_name = 'news/news_list.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
