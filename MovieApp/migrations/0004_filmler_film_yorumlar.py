# Generated by Django 3.2.12 on 2022-04-22 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0003_filmler_diller'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmler',
            name='film_yorumlar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MovieApp.yorumlar'),
        ),
    ]
