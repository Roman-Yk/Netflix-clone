# Generated by Django 4.0.7 on 2022-12-25 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='static/img/movies_img'),
        ),
    ]
