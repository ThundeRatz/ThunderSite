"""
ThunderSite - ThundeRatz

Projects Models
Daniel Nery Silva de Oliveira

01/2018
"""

from django.db import models
from ckeditor.fields import RichTextField

## Projects
class SuperCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'super categories'

class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    super_category = models.ForeignKey(SuperCategory, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

def project_thumbnail_path(instance, filename):
    return 'projects/' + instance.name + '/thumb_' + filename

class Project(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True, help_text="URL name: <em>thunderatz.org/projects/&lt;slug&gt;</em>")
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    logo = models.ImageField(upload_to='project_logos')
    typography = models.ImageField(upload_to='project_typography')
    thumbnail = models.ImageField(upload_to=project_thumbnail_path)
    debut_year = models.PositiveSmallIntegerField()
    gold = models.PositiveSmallIntegerField(default=0)
    silver = models.PositiveSmallIntegerField(default=0)
    bronze = models.PositiveSmallIntegerField(default=0)
    description = RichTextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

def project_images_path(instance, filename):
    return 'projects/' + instance.project.name + '/' + filename

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pictures')
    image = models.ImageField(upload_to=project_images_path)
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.description
