# Generated by Django 4.0.7 on 2022-12-25 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_age_movie_category_movie_rating_movie_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
    ]
