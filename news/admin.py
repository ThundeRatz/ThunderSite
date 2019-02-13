from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "slug",
        "author",
        "cover_image",
        "intro_image",
        "text",
        "visible",
        "created_date",
        "published_date",
    )
    list_display = ("title", "author", "created_date", "visible")
    prepopulated_fields = {"slug": ("title",)}
