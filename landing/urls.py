from django.urls import path
from landing import views

app_name = 'landing'

urlpatterns = [
    path('', views.soon, name='soon'),
    path('teste/', views.IndexView.as_view(), name='index'),
]
