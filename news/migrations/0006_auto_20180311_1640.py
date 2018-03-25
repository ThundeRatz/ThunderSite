# Generated by Django 2.0.1 on 2018-03-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180309_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='intro_image',
            field=models.ImageField(blank=True, help_text='Imagem que vai logo antes do começo do texto da notícias', null=True, upload_to='news_intro'),
        ),
        migrations.AlterField(
            model_name='news',
            name='cover_image',
            field=models.ImageField(help_text='Imagem que vai no preview da noticia, no topo da pagina de detalhes e no final do texto da noticia', upload_to='news_cover'),
        ),
    ]