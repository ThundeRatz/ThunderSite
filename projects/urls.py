"""
ThunderSite - ThundeRatz

Projects Pages URL patterns
Daniel Nery Silva de Oliveira

01/2018
"""

from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.ProjectListView.as_view(), name='index'),
    path('<slug:slug>', views.ProjectDetailView.as_view(), name='detail'),
]
