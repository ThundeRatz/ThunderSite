# Generated by Django 2.0.1 on 2018-04-16 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("projects", "0006_auto_20180416_2027")]

    operations = [
        migrations.RemoveField(model_name="project", name="card_and_top"),
        migrations.RemoveField(model_name="project", name="card_image"),
        migrations.RemoveField(model_name="project", name="cover_image"),
        migrations.RemoveField(model_name="project", name="thumbnail"),
    ]
