# Generated by Django 3.2.12 on 2022-04-22 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0004_filmler_film_yorumlar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmler',
            name='film_yorumlar',
        ),
    ]
