# Generated by Django 4.2.7 on 2023-11-18 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_email_user_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]