"""
ThunderSite - ThundeRatz

News Models
Daniel Nery Silva de Oliveira

01/2018
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username="deleted")[0]


class News(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.SET(get_sentinel_user))
    title = models.CharField(max_length=256)
    slug = models.SlugField(
        unique=True, help_text="URL name: <em>thunderatz.org/news/&lt;slug&gt;</em>"
    )
    text = RichTextUploadingField(
        # extra_plugins=["youtube"],
        help_text='<h1><strong>Se upar imagens, colocar a classe "body-image" nela na aba Advanced!</strong></h1>',
    )

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    cover_image = models.ImageField(
        upload_to="news_cover",
        help_text="Imagem que vai no preview da noticia, no topo da pagina de detalhes e no final do texto da noticia, <strong>Cuidado</strong> com imagens muito grandes! Menos de 1MB é mais que suficiente.",
    )
    intro_image = models.ImageField(
        upload_to="news_intro",
        help_text="Imagem que vai logo antes do começo do texto da notícias",
        blank=True,
        null=True,
    )

    visible = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "news"
        ordering = ["-published_date"]

    def __str__(self):
        return self.title
