# Generated by Django 4.1.5 on 2023-01-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0018_alter_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='tariff',
            field=models.CharField(choices=[('default', 'default'), ('plus', 'plus'), ('premium', 'premium')], max_length=15, null=True),
        ),
    ]
