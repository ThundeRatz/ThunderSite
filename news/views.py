"""
ThunderSite - ThundeRatz

News Pages Views
Daniel Nery Silva de Oliveira

01/2018
"""

from django.views.generic import View, TemplateView, ListView, DetailView


# TODO put the List and DetailView, with the models
class NewsListView(TemplateView):
    template_name = 'news/news_list.html'

class NewsDetailView(TemplateView):
    template_name = 'news/news_detail.html'
