# Generated by Django 2.0.1 on 2018-03-05 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20180303_1937'),
        ('projects', '0008_auto_20180223_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bold',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.Member'),
        ),
    ]