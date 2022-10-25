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
    logo = models.ImageField(upload_to="sponsors")

    def __str__(self):
        return self.name


## Timeline events
class Event(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField(unique=True)
    text = RichTextField()
    image = models.ImageField(upload_to="events")

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title


## About texts
class About(models.Model):
    CHOICES = (("A", "Team"), ("B", "Workshop"))

    type = models.CharField(max_length=1, choices=CHOICES, unique=True)
    text = RichTextField()
    title = models.CharField(max_length=32)

    image1 = models.ImageField(upload_to="about")
    image2 = models.ImageField(upload_to="about")
    image3 = models.ImageField(upload_to="about")

    def __str__(self):
        return self.title


class Recruitment(models.Model):
    title = models.CharField(max_length=64)
    button = models.TextField(help_text="Cole o script do Typeform aqui", default="")
    image = models.ImageField(upload_to="ps")
    isOpen = models.BooleanField(default=False)
    info = RichTextField()

    def __str__(self):
        return self.title


class ProgressBar(models.Model):
    name = models.CharField(max_length=64)
    current_value = models.IntegerField()
    maximum_value = models.IntegerField()
    pix_link = models.URLField(default="")
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name} {self.current_value}/{self.maximum_value}"
