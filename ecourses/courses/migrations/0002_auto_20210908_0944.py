# Generated by Django 3.2.6 on 2021-09-08 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.RenameField(
            model_name='groupchat',
            old_name='id_course',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='id_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='user_id',
            new_name='user',
        ),
    ]
