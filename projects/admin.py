from django.contrib import admin
from .models import SuperCategory, Category, Project, ProjectImage, Board

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    prepopulated_fields = { 'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'super_category', 'description')

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name',)}

admin.site.register(SuperCategory)
admin.site.register(ProjectImage)
