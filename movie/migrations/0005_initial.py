# Generated by Django 4.2.7 on 2023-11-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0004_delete_movie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('year', models.DateField()),
                ('region', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=50)),
                ('lasting', models.IntegerField()),
            ],
        ),
    ]
