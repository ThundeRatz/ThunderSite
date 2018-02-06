from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'cover_image', 'text', 'visible', 'created_date', 'published_date')
    list_display = ('title', 'author', 'created_date', 'visible')
