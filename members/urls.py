"""
ThunderSite - ThundeRatz

Members Pages URL patterns
Daniel Nery Silva de Oliveira

02/2018
"""

from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    path('', views.MemberListView.as_view(), name='members_list'),
]
