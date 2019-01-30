"""
ThunderSite - ThundeRatz

News Pages Views
Daniel Nery Silva de Oliveira

01/2018
"""

from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import News


class NewsListView(ListView):
    model = News
    context_object_name = "news_list"
    template_name = "news/news_list.html"
    paginate_by = 14


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"
