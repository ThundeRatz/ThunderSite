# Generated by Django 2.0.1 on 2018-03-05 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_project_bold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='boards',
            field=models.ManyToManyField(blank=True, null=True, to='projects.Board'),
        ),
        migrations.AlterField(
            model_name='project',
            name='bold',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Member'),
        ),
    ]