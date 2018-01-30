from django.shortcuts import render, get_object_or_404
from django.views.generic import View, TemplateView, ListView, DetailView
from .models import Project, SuperCategory, Category

# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = 'projects/index.html'

class ProjectListView(ListView):
    template_name = 'projects/project_list.html'
    context_object_name = 'project_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cards'] = [x for x in range(1,8)]
        context['cat'] = self.category
        context['subcat'] = Category.objects.filter(super_category=self.category)

        return context

    def get_queryset(self):
        self.category = get_object_or_404(SuperCategory, name=self.kwargs['category'])
        return Project.objects.filter(category__super_category=self.category)

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
