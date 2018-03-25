# Generated by Django 2.0.1 on 2018-02-23 00:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180210_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(help_text='URL name: <em>thunderatz.org/projects/boards/&lt;slug&gt;</em>', unique=True)),
                ('thumbnail', models.ImageField(upload_to='board_thumbnails')),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['is_active', 'name']},
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(help_text='URL name: <em>thunderatz.org/projects/robots/&lt;slug&gt;</em>', unique=True),
        ),
        migrations.AddField(
            model_name='board',
            name='robots',
            field=models.ManyToManyField(to='projects.Project'),
        ),
    ]