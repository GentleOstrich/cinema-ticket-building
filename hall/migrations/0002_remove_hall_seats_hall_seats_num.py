# Generated by Django 4.2.7 on 2023-12-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hall', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hall',
            name='seats',
        ),
        migrations.AddField(
            model_name='hall',
            name='seats_num',
            field=models.IntegerField(default=0),
        ),
    ]
