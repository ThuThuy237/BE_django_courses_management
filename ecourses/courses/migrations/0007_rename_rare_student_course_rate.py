# Generated by Django 3.2.6 on 2021-09-09 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210909_1528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_course',
            old_name='rare',
            new_name='rate',
        ),
    ]
