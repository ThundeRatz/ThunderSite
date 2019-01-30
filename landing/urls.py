"""
ThunderSite - ThundeRatz

Landing Page URL patterns
Daniel Nery Silva de Oliveira

01/2018
"""

from django.urls import path
from landing import views

app_name = "landing"

urlpatterns = [path("", views.IndexView.as_view(), name="index")]
