"""
ThunderSite - ThundeRatz

Projects Pages URL patterns
Daniel Nery Silva de Oliveira

01/2018
"""

from django.urls import path, reverse_lazy
from django.views.generic import RedirectView
from . import views

app_name = "projects"

urlpatterns = [
    path("", RedirectView.as_view(url=reverse_lazy("projects:robots"))),
    path("robots/", views.ProjectListView.as_view(), name="robots"),
    path("robots/<slug:slug>", views.ProjectDetailView.as_view(), name="robot_detail"),
    path("boards/", views.BoardListView.as_view(), name="boards"),
    path("boards/<slug:slug>", views.BoardDetailView.as_view(), name="board_detail"),
]
