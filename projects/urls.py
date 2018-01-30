from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('<category>/', views.ProjectListView.as_view(), name='category'),
    path('<pk>', views.ProjectDetailView.as_view(), name='detail'),
]
