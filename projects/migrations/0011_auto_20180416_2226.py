# Generated by Django 2.0.1 on 2018-04-17 01:26

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [("projects", "0010_auto_20180416_2141")]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="card_image",
            field=models.ImageField(
                default="1000x1000.png", upload_to=projects.models.project_card_path
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="cover_image",
            field=models.ImageField(
                default="1000x1000.png", upload_to=projects.models.project_cover_path
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="logo",
            field=models.ImageField(default="1000x1000.png", upload_to="project_logos"),
        ),
        migrations.AlterField(
            model_name="project",
            name="typography",
            field=models.ImageField(
                default="1000x1000.png", upload_to="project_typography"
            ),
        ),
    ]
