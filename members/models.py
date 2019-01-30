"""
ThunderSite - ThundeRatz

Members Models
Daniel Nery Silva de Oliveira

02/2018
"""

from django.db import models
from django.core.exceptions import ValidationError


def member_picture_path(instance, filename):
    ext = filename.split(".")[-1]
    return "members/" + instance.nickname + "." + ext


class Member(models.Model):
    CHOICES = (
        ("EL", "Elétrica"),
        ("MC", "Mecânica"),
        ("CP", "Computação"),
        ("DM", "Design e Marketing"),
        ("AF", "Administrativo e Financeiro"),
    )

    name = models.CharField(max_length=128)
    nickname = models.CharField(max_length=64, unique=True)
    area = models.CharField(max_length=2, choices=CHOICES)
    area_captain = models.BooleanField(default=False)
    team_captain = models.BooleanField(default=False)
    picture = models.ImageField(upload_to=member_picture_path, default="1000x1000.png")
    facebook = models.URLField(blank=True, null=True)
    email = models.EmailField()
    entry_year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ["-team_captain", "-area_captain", "name"]

    def __str__(self):
        return self.name

    def clean(self):
        if self.area_captain is True and self.team_captain is True:
            raise ValidationError(
                {
                    "area_captain": ValidationError("Choose only one!", code="invalid"),
                    "team_captain": ValidationError("Choose only one!", code="invalid"),
                }
            )
        if self.area_captain is True and self.area == "AF":
            raise ValidationError(
                {
                    "area_captain": ValidationError(
                        "This area doesn't have captains!", code="invalid"
                    )
                }
            )
