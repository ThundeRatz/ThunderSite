# Generated by Django 2.0.8 on 2020-01-30 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180418_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
