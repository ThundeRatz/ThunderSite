"""
ThunderSite - ThundeRatz

Landing Page models
Daniel Nery Silva de Oliveira

01/2018
"""

from django.db import models
from ckeditor.fields import RichTextField

## Sponsors
class Quota(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Sponsor(models.Model):
    name = models.CharField(max_length=128, unique=True)
    website = models.URLField(unique=True)
    quota = models.ForeignKey(Quota, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='sponsors')

    def __str__(self):
        return self.name

## Timeline events
class Event(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField(unique=True)
    text = RichTextField()
    image = models.ImageField(upload_to='events')

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
