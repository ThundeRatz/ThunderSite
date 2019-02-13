# Generated by Django 2.0.1 on 2018-04-16 22:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import projects.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("members", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "slug",
                    models.SlugField(
                        help_text="URL name: <em>thunderatz.org/projects/boards/&lt;slug&gt;</em>",
                        unique=True,
                    ),
                ),
                (
                    "thumbnail",
                    models.ImageField(upload_to=projects.models.board_thumbnail_path),
                ),
                ("description", ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name="BoardImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to=projects.models.board_images_path),
                ),
                ("description", models.CharField(max_length=512)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pictures",
                        to="projects.Board",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.CharField(max_length=512)),
            ],
            options={"verbose_name_plural": "categories"},
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "slug",
                    models.SlugField(
                        help_text="URL name: <em>thunderatz.org/projects/robots/&lt;slug&gt;</em>",
                        unique=True,
                    ),
                ),
                ("logo", models.ImageField(upload_to="project_logos")),
                ("typography", models.ImageField(upload_to="project_typography")),
                (
                    "cover_image",
                    models.ImageField(upload_to=projects.models.project_cover_path),
                ),
                (
                    "card_image",
                    models.ImageField(upload_to=projects.models.project_card_path),
                ),
                ("debut_year", models.PositiveSmallIntegerField()),
                ("gold", models.PositiveSmallIntegerField(default=0)),
                ("silver", models.PositiveSmallIntegerField(default=0)),
                ("bronze", models.PositiveSmallIntegerField(default=0)),
                ("description", ckeditor.fields.RichTextField()),
                ("is_active", models.BooleanField(default=True)),
                ("boards", models.ManyToManyField(blank=True, to="projects.Board")),
                (
                    "bold",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="members.Member",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="projects.Category",
                    ),
                ),
            ],
            options={"ordering": ["-is_active", "name"]},
        ),
        migrations.CreateModel(
            name="ProjectImage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to=projects.models.project_images_path),
                ),
                ("description", models.CharField(max_length=512)),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pictures",
                        to="projects.Project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SuperCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64, unique=True)),
            ],
            options={"verbose_name_plural": "super categories"},
        ),
        migrations.AddField(
            model_name="category",
            name="super_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="projects.SuperCategory"
            ),
        ),
    ]
