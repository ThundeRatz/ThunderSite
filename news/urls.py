"""
ThunderSite - ThundeRatz

News Pages URL patterns
Daniel Nery Silva de Oliveira

02/2018
"""

from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('<slug:slug>', views.NewsDetailView.as_view(), name='news_detail'),
]
