"""
ThunderSite - ThundeRatz

News Models
Daniel Nery Silva de Oliveira

01/2018
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor.fields import RichTextField

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET(get_sentinel_user))
    title = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, help_text="URL name: <em>thunderatz.org/news/&lt;slug&gt;</em>")
    text = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    visible = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='news_cover')

    class Meta:
        verbose_name_plural = 'news'
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.visible = False
        self.save()

    def hide(self):
        self.visible = False
        self.save()

    def show(self):
        self.visible = True
        self.save()

    def __str__(self):
        return self.title
