# Generated by Django 4.0.7 on 2022-12-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0008_movie_homepage_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(choices=[('Movie', 'movie'), ('Series', 'series')], max_length=10, null=True),
        ),
    ]
