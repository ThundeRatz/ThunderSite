from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=128)
    nickname = models.CharField(max_length=64)

    def __str__(self):
        return self.name
