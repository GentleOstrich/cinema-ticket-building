# Generated by Django 4.2.7 on 2023-11-17 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_id_user_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_password',
            new_name='username',
        ),
    ]
