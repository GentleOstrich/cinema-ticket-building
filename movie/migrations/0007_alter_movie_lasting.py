# Generated by Django 4.2.7 on 2023-12-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='lasting',
            field=models.CharField(max_length=10),
        ),
    ]
